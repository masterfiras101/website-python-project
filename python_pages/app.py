# from rembg import remove
# import mediapipe as mp
# import cv2
# from pycaw.pycaw import AudioUtilities , IAudioEndpointVolume
# from comtypes import  CLSCTX_ALL
# from ctypes import cast , POINTER

import contextlib
from io import BytesIO
from streamlit_cropper import st_cropper
import pandas as pd

import numpy as np
import requests
from PIL import Image, ImageEnhance, ImageOps

import streamlit as st # this important library for analysis and showing the data


# st.set_page_config(
#     page_title="الرئيسية",
#     page_icon="🖼",  
# )

def functionall():

    VERSION = "0.7.0"

    # def volume_control():
    #     cap = cv2.VideoCapture(0)
    #     frame_placeholder = st.empty()
    #     stop_button_pressed = st.button("اوقف العملية")
    #     mpHands = mp.solutions.hands
    #     hands =  mpHands.Hands(min_detection_confidence = 0.7)
    #     mpDraw = mp.solutions.drawing_utils
    #     devices = AudioUtilities.GetSpeakers()
    #     interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    #     volume = cast(interface, POINTER(IAudioEndpointVolume))
    #     volrange = volume.GetVolumeRange()
    #     minvol = volrange[0]
    #     maxvol = volrange[1]
    #     while cap.isOpened() and not stop_button_pressed:
    #         ret, frame = cap.read()
    #         if not ret:
    #             st.write("Video Capture Ended")
    #             break
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         frame_placeholder.image(frame,channels="RGB")
    #         results = hands.process(frame)
    #         lmList = []
    #         if results.multi_hand_landmarks:
    #             for handLms in results.multi_hand_landmarks:
    #                 for id, lm in enumerate(handLms.landmark):
    #                     h, w, c = frame.shape
    #                     cx, cy = int(lm.x * w), int(lm.y * h)
    #                     lmList.append([id, cx, cy])
    #                     if len(lmList) == 21:
    #                         x1, y1 = lmList[4][1],lmList[4][2]
    #                         x2, y2 = lmList[8][1],lmList[8][2]
    #                         cx, cy  = (x1 + x2)// 2, (y1 + y2)// 2
    #                         cv2.circle(frame, (x1, y1), 8, (255, 0, 255), cv2.FILLED)
    #                         cv2.circle(frame, (x2, y2), 8, (255, 0, 255), cv2.FILLED)
    #                         cv2.line(frame, (x1, y1), (x2, y2), (0 ,0 ,0), 3)
    #                         cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
    #                         length = math.hypot(x2 - x1 , y2 - y1)
    #                         if length > 50 :
    #                             cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    #                         if length > 200 :
    #                             cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    #                         vol = np.interp(length, [50, 200], [minvol, maxvol])                 
    #                         volume.SetMasterVolumeLevel(vol, None)
    #         if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
    #             break
    #     cap.release()
    #     cv2.destroyAllWindows()








    # ---------- SIDEBAR ---------- for get html page and set it in side left 
    # with open("sidebar.html", "r", encoding="UTF-8") as sidebar_file:
    #     sidebar_html = sidebar_file.read().replace("{VERSION}", VERSION)

    # with st.sidebar:
    #     with st.expander("الخدمات التي يقدمها التطبيق"):
    #         st.info(
    #             "* تحميل صورة, ياخذ صورة واحدة من الكاميرا او عبر رابط لصورة \n"
    #             "*  خاصية قص\n"
    #             "* خاصية ابعاد الخلفية\n"
    #             "*خاصية مرآه\n"
    #             "* تحويل الى تدرج رمادي او اسود او ابيض\n"
    #             "* تدوير\n"
    #             "* تغير السطوع, وتشبع اللون, وخاصية التباين, وخاصية حدة اللون\n"
    #             "* توليد صورة عشوائية من مزود الصور\n"
    #             "* تحميل الصورة"
    #         )
    #     st.components.v1.html(sidebar_html, height=500,width=330)



    # ---------- HEADER ----------
    # st.title("👋 مرحبا بك في تطبيقنا الرائع ")


    # ---------- FUNCTIONS ----------
    def _reset(key: str) -> None:
        if key == "all":
            st.session_state["rotate_slider"] = 0
            st.session_state["brightness_slider"] = st.session_state[
                "saturation_slider"
            ] = st.session_state["contrast_slider"] = 100
            st.session_state["bg"] = st.session_state["crop"] = st.session_state[
                "mirror"
            ] = st.session_state["gray_bw"] = 0
        elif key == "rotate_slider":
            st.session_state["rotate_slider"] = 0
        elif key == "checkboxes":
            st.session_state["crop"] = st.session_state["mirror"] = st.session_state[
                "gray_bw"
            ] = 0
        else:
            st.session_state[key] = 100


    def _randomize() -> None:
        st.session_state["mirror"] = np.random.choice([0, 1])
        st.session_state["rotate_slider"] = np.random.randint(0, 360)
        st.session_state["brightness_slider"] = np.random.randint(0, 200)
        st.session_state["saturation_slider"] = np.random.randint(0, 200)
        st.session_state["contrast_slider"] = np.random.randint(0, 200)
        st.session_state["sharpness_slider"] = np.random.randint(0, 200)


    # ---------- OPERATIONS ----------

    option = st.radio(
        label="تحميل صورة ,التقاط صورة بواسطة كاميرا الجهاز, جلب الصورة عبر رابط",
        options=(
            "تحميل صورة من ملف ⬆️",
            "التقاط صورة عبر الكاميرا📷",
            "جلب صورة من رابط 🌐",
            "التحكم بالصووت :loud_sound:",   
        ),
        # help="Uploaded images are deleted from the server when you\n* upload another image\n* clear the file uploader\n* close the browser tab",
    )

    if option == "التقاط صورة عبر الكاميرا📷":
        upload_img = st.camera_input(
            label="التقط صورة",
        )
        mode = "camera"
        
        
    elif option == "التحكم بالصووت :loud_sound:":
            st.button(
            "التحكم بالصوت ",
            # on_click=volume_control,
            # type="secondary", 
            # disabled=False, 
            # use_container_width=False

        )  
    
        
    elif option == "تحميل صورة من ملف ⬆️":
        upload_img = st.file_uploader(
            label="اختر هنا من اجل تحميل الصورة",
            type=["bmp", "jpg", "jpeg", "png", "svg"],
        )
        mode = "upload"

    elif option == "جلب صورة من رابط 🌐":
        url = st.text_input(
            "رابط الصورة",
            key="url",
        )
        mode = "url"

        if url != "":
            try:
                response = requests.get(url)
                upload_img = Image.open(BytesIO(response.content))
            except:
                st.error("يبدو أن عنوان  الرابط لايمثل التغيير السابق الصحيح")

    with contextlib.suppress(NameError):
        if upload_img is not None:
            pil_img = (
                upload_img.convert("RGB")
                if mode == "url"
                else Image.open(upload_img).convert("RGB")
            )
            img_arr = np.asarray(pil_img)

            # ---------- PROPERTIES ----------
            st.image(img_arr, use_column_width="auto", caption="الصورة المحملة")
            st.text(
                f"العرض الاصلي = {pil_img.size[0]}px   الطول = {pil_img.size[1]}px"
            )

            # st.caption("All changes are applied on top of the previous change.")
            st.caption(".يتم تطبيق كافة التغييرات فوق التغيير السابق")
            

            # ---------- CROP ----------
            st.text("خاصية القص ✂️")
            cropped_img = st_cropper(Image.fromarray(img_arr), should_resize_image=True)
            st.text(
                f" عرض الصورة بعد القص = px{cropped_img.size[0]} &  الطول = px{cropped_img.size[1]}"
            )

            with st.container():
                lcol, rcol = st.columns(2)
                if lcol.checkbox(
                    label="اختر من هنا خاصية القص",
                    help="لقص وتعديل الصورة",
                    key="crop",
                ):
                    image = cropped_img
                else:
                    image = Image.fromarray(img_arr)

                # ---------- REMOVE BACKGROUND ----------
                if lcol.checkbox(
                    label="ابعاد الخلفية؟",
                    help="اختر هنا لابعاد خلفية الصورة",
                    key="bg",
                ):
                    # image = remove(image)
                    image = (image)

                # ---------- MIRROR ----------
                if lcol.checkbox(
                    label="صورة مرآة",
                    help="اختر من اجل صورة شبة مرآة",
                    key="mirror",
                ):
                    image = ImageOps.mirror(image)

                # ---------- GRAYSCALE / B&W ----------
                flag = True

                if lcol.checkbox(
                    "تحويل الى تدرج رمادي / اسود وابيض ؟🔲",
                    key="gray_bw",
                    help="اختر هنا من اجل التحويل الى تدرج رمادي او اسود&ابييض",
                ):
                    mode = "L"
                    if (
                        lcol.radio(
                            label="تدرج رمادي او اسود&ابيض ",
                            options=("تدرج رمادي", "اسود & ابيض"),
                        )
                        == "Grayscale"
                    ):
                        image = image.convert(mode)
                    else:
                        flag = False
                        lcol.warning(
                            "بعض الخاصيات غير متوفرة في الصورة السوداء والبيضاء."
                        )
                        thresh = np.array(image).mean()
                        fn = lambda x: 255 if x > thresh else 0
                        image = image.convert(mode).point(fn, mode="1")
                else:
                    mode = "RGB"
                rcol.image(
                    image,
                    use_column_width="auto",
                )

                if lcol.button(
                    "↩️ العودة الى الاصلية",
                    on_click=_reset,
                    use_container_width=True,
                    kwargs={"key": "checkboxes"},
                ):
                    lcol.success("تم العودة الى الصورة الاصلية !")

            st.markdown("""---""")

            # ---------- OTHER OPERATIONS ----------
            # ---------- 1ST ROW ----------
            with st.container():
                lcol, mcol, rcol = st.columns(3)

                # ---------- ROTATE ----------
                if "rotate_slider" not in st.session_state:
                    st.session_state["rotate_slider"] = 0
                degrees = lcol.slider(
                    "🔁تدوير الصورة في اتجاة عقارب الساعة",
                    min_value=0,
                    max_value=360,
                    value=st.session_state["rotate_slider"],
                    key="rotate_slider",
                )
                rotated_img = image.rotate(360 - degrees)
                lcol.image(
                    rotated_img,
                    use_column_width="auto",
                    caption=f"دورة الصورة  بدرجة  : %{degrees}  في اتجاة اعقارب الساعة  ",
                )
                if lcol.button(
                    "↩️ العودة من التدوير",
                    on_click=_reset,
                    use_container_width=True,
                    kwargs={"key": "rotate_slider"},
                ):
                    lcol.success("!تم العودة من التدوير الى الاصلية")

                if flag:
                    # ---------- BRIGHTNESS ----------
                    if "brightness_slider" not in st.session_state:
                        st.session_state["brightness_slider"] = 100
                    brightness_factor = mcol.slider(
                        "قم بتغيير السطوع 💡",
                        min_value=0,
                        max_value=200,
                        value=st.session_state["brightness_slider"],
                        key="brightness_slider",
                    )
                    brightness_img = np.asarray(
                        ImageEnhance.Brightness(rotated_img).enhance(
                            brightness_factor / 100
                        )
                    )
                    mcol.image(
                        brightness_img,
                        use_column_width="auto",
                        caption=f"نسبة السطوع  : % {brightness_factor}",
                    )
                    if mcol.button(
                        "↩️ العودة من السطوع",
                        on_click=_reset,
                        use_container_width=True,
                        kwargs={"key": "brightness_slider"},
                    ):
                        mcol.success("!تم العودة من السطوع الى الاصلية")

                    # ---------- SATURATION ----------
                    if "saturation_slider" not in st.session_state:
                        st.session_state["saturation_slider"] = 100
                    saturation_factor = rcol.slider(
                        "قم بتغيير نسبة التشبع",
                        min_value=0,
                        max_value=200,
                        value=st.session_state["saturation_slider"],
                        key="saturation_slider",
                    )
                    saturation_img = np.asarray(
                        ImageEnhance.Color(Image.fromarray(brightness_img)).enhance(
                            saturation_factor / 100
                        )
                    )
                    rcol.image(
                        saturation_img,
                        use_column_width="auto",
                        caption=f" % نسبة تشبع اللون :  {saturation_factor}",
                    )
                    if rcol.button(
                        "↩️ رجوع",
                        on_click=_reset,
                        use_container_width=True,
                        kwargs={"key": "saturation_slider"},
                    ):
                        rcol.success("تم العودة من من خاصية التشبع!")

                    st.markdown("""---""")

                    # ---------- 2ND ROW ----------
                    with st.container():
                        lcol, mcol, rcol = st.columns(3)
                        # ---------- CONTRAST ----------
                        if "contrast_slider" not in st.session_state:
                            st.session_state["contrast_slider"] = 100
                        contrast_factor = lcol.slider(
                            "قم بتغيير تباين الصورة",
                            min_value=0,
                            max_value=200,
                            value=st.session_state["contrast_slider"],
                            key="contrast_slider",
                        )
                        contrast_img = np.asarray(
                            ImageEnhance.Contrast(Image.fromarray(saturation_img)).enhance(
                                contrast_factor / 100
                            )
                        )
                        lcol.image(
                            contrast_img,
                            use_column_width="auto",
                            caption=f"نسبة التباين : % {contrast_factor}",
                        )
                        if lcol.button(
                            "↩️ العودة من التباين",
                            on_click=_reset,
                            use_container_width=True,
                            kwargs={"key": "contrast_slider"},
                        ):
                            lcol.success("!تم العودة من التبابن الى الاصلية")

                        # ---------- SHARPNESS ----------
                        if "sharpness_slider" not in st.session_state:
                            st.session_state["sharpness_slider"] = 100
                        sharpness_factor = mcol.slider(
                            "قم بتغيير حدة الصورة ",
                            min_value=0,
                            max_value=200,
                            value=st.session_state["sharpness_slider"],
                            key="sharpness_slider",
                        )
                        sharpness_img = np.asarray(
                            ImageEnhance.Sharpness(Image.fromarray(contrast_img)).enhance(
                                sharpness_factor / 100
                            )
                        )
                        mcol.image(
                            sharpness_img,
                            use_column_width="auto",
                            caption=f"نسبة الحدة :  % {sharpness_factor}",
                        )
                        if mcol.button(
                            "↩️ العودة من حدة الصورة",
                            on_click=_reset,
                            use_container_width=True,
                            kwargs={"key": "sharpness_slider"},
                        ):
                            mcol.success("تم العودة  من وضع الحدة الى الاصلية!")

            st.markdown("""---""")

            # ---------- FINAL OPERATIONS ----------
            st.subheader("مشاهدة النتائج")
            lcol, rcol = st.columns(2)
            lcol.image(
                img_arr,
                use_column_width="auto",
                caption=f"الصورة الاصلية ({pil_img.size[0]} x {pil_img.size[1]})",
            )

            try:
                final_image = sharpness_img
            except NameError:
                final_image = rotated_img

            rcol.image(
                final_image,
                use_column_width="auto",
                caption=f"الصورة الناتجة ({final_image.shape[1]} x {final_image.shape[0]})"
                if flag
                else f"الصورة الناتجة ({final_image.size[1]} x {final_image.size[0]})",
            )

            if flag:
                Image.fromarray(final_image).save("final_image.png")
            else:
                final_image.save("final_image.png")

            col1, col2, col3 = st.columns(3)
            if col1.button(
                "↩️ الغاء كافة التعديلات",
                on_click=_reset,
                use_container_width=True,
                kwargs={"key": "all"},
            ):
                st.success(body="! تم الغاء كافة التعديلات", icon="↩️")
                
            if col2.button(
                "🔀 فاجئني بتوليد صورة",
                on_click=_randomize,
                use_container_width=True,
            ):
                st.success(body="توليد صورة عشوائيا", icon="🔀")
            with open("final_image.png", "rb") as file:
                col3.download_button(
                    "💾تحميل الصورة",
                    data=file,
                    mime="image/png",
                    use_container_width=True,
                )
