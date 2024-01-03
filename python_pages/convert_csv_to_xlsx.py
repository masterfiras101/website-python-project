import streamlit as st
import pandas as pd
import zipfile
import tempfile
import os
import base64
from datetime import datetime


def converCsv():

    # Upload comma-separated CSV file(s)
    st.title(" zip  أو مجموعة من الملفات بصيغة csv  قم برفع ملف بصيغة")
    uploaded_files = st.file_uploader(
        "file csv",
        accept_multiple_files=True,
        type=["csv", "zip"],
    )

    # Option to toggle automatic type conversion (e.g. 1,000 to 1000)
    auto_conversion = st.toggle(
        " تحويل تلقائي >> للمساعدة قم بالتأشير على علامة الإستفهام",
        value=False,
        help="في بعض الأحيان، يتم تخزين الأرقام كنص في ملفات CSV. قد لا تعمل المحددات وفواصل الآلاف بشكل صحيح في هذه الحالة. سيقوم هذا الخيار بتحويلها تلقائيًا إلى أرقام. إذا لم تكن متأكدًا، فاترك هذا الخيار معطلاً وتحقق من النتيجة.",
    )

    # Initiate data dictionary
    data = {}


    # Filename function
    def file_name():
        return str(datetime.now().strftime("%Y-%m-%d_%H-%M_csv_to_xlsx"))


    if len(uploaded_files) > 0:
        with st.status("عرف الملفات التي في حالة القراءة"):
            # Iterate through each uploaded file and check if they are CSV or ZIP
            for uploaded_file in uploaded_files:
                if uploaded_file.name.endswith(".csv"):
                    if auto_conversion:
                        st.write(f"📄  الملف يقرأ: **{uploaded_file.name}**")
                        df = pd.read_csv(uploaded_file)

                        # Automatic conversion to numeric logic
                        for col in df.columns:
                            try:
                                df[col] = pd.to_numeric(
                                    df[col].str.replace(",", "").str.replace('"', ""),
                                    errors="raise",
                                )
                                st.write(
                                    f"⚠️ تحويل العمود تلقائيًا إلى **{uploaded_file.name}**: {col}"
                                )
                            except:
                                pass

                        data[uploaded_file.name] = df
                    else:
                        st.write(f"📄 الملف يقرأ: **{uploaded_file.name}**")
                        data[uploaded_file.name] = pd.read_csv(uploaded_file)

                elif uploaded_file.name.endswith(".zip"):
                    with tempfile.TemporaryDirectory() as tmpdirname:
                        with zipfile.ZipFile(uploaded_file) as z:
                            z.extractall(tmpdirname)
                            for filename in z.namelist():
                                if filename.endswith(".csv"):
                                    if auto_conversion:
                                        st.write(f"📄 الملف يقرأ: **{uploaded_file.name}**")
                                        df = pd.read_csv(os.path.join(tmpdirname, filename))

                                        # Automatic conversion to numeric logic
                                        for col in df.columns:
                                            try:
                                                df[col] = pd.to_numeric(
                                                    df[col]
                                                    .str.replace(",", "")
                                                    .str.replace('"', ""),
                                                    errors="يرفع",
                                                )
                                                st.write(
                                                    f"⚠️ تحويل العمود تلقائيًا إلى **{filename}**: {col}"
                                                )
                                            except:
                                                pass

                                        data[filename] = df
                                    else:
                                        st.write(f"📄 الملف يقرأ: **{filename}**")
                                        data[filename] = pd.read_csv(
                                            os.path.join(tmpdirname, filename)
                                        )
                                else:
                                    st.warning(
                                        f"⚠️ الملف : **{filename}** CSV لايكون من نوع ملف"
                                    )

    # Preview
    if len(data) > 0:
        with st.expander("معاينة البيانات"):
            preview_selector = st.selectbox("معاينة", list(data.keys()))
            st.dataframe(data[preview_selector])

    # Download
    if len(data) == 0:
        st.info("zip أو csv رفع ملف")
    elif len(data) > 1:
        download_col1, download_col2 = st.columns(2)

        with download_col1:
            with st.expander("ملف واحد  : 1 الخيار", expanded=True):
                st.write(
                    "قم بتنزيل كافة البيانات كملف XSLX واحد، مع كل ملف CSV كورقة منفصلة"
                )
                # Download as single file with multiple sheets
                with tempfile.TemporaryDirectory() as tmpdirname:
                    with pd.ExcelWriter(
                        os.path.join(tmpdirname, f"{file_name()}.xlsx")
                    ) as writer:
                        for key, value in data.items():
                            # Create sheet name from filename, emitting the extension
                            sheet_name = key[:-4][
                                :31
                            ]  # Excel sheet name cannot be longer than 31 characters
                            value.to_excel(writer, sheet_name=sheet_name, index=False)
                    with open(os.path.join(tmpdirname, f"{file_name()}.xlsx"), "rb") as f:
                        bytes_data = f.read()
                    b64 = base64.b64encode(bytes_data).decode()
                    href = f"data:file/xlsx;base64,{b64}"
                    st.download_button(
                        label="تحميل",
                        data=bytes_data,
                        file_name=f"{file_name()}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True,
                    )

                # st.write("Download data as individual XLSX files with a single sheet, put together in a ZIP file.")
        with download_col2:
            with st.expander("ملفات منفصلة : 2 الخيار", expanded=True):
                st.write(
                    "zip فردية بورقة واحدة محمعمة معآ في ملف xlsx قم بتنزيل البيانات كملفات"
                )
                # Download as separate files in a ZIP 
                with tempfile.TemporaryDirectory() as tmpdirname:
                    with zipfile.ZipFile(
                        os.path.join(tmpdirname, f"{file_name()}.zip"), "w"
                    ) as z:
                        for key, value in data.items():
                            xlsx_filename = f"{key[:-4]}.xlsx"
                            value.to_excel(
                                os.path.join(tmpdirname, xlsx_filename), index=False
                            )
                            z.write(
                                os.path.join(tmpdirname, xlsx_filename),
                                arcname=xlsx_filename,
                            )
                    with open(os.path.join(tmpdirname, f"{file_name()}.zip"), "rb") as f:
                        bytes_data = f.read()
                    b64 = base64.b64encode(bytes_data).decode()
                    href = f"data:file/zip;base64,{b64}"
                    st.download_button(
                        label="تحميل",
                        data=bytes_data,
                        file_name=f"{file_name()}.zip",
                        mime="application/zip",
                        use_container_width=True,
                    )

    else:
        # Download
        with tempfile.TemporaryDirectory() as tmpdirname:
            single_filename = list(data.keys())[0][:-4] + ".xlsx"
            data[list(data.keys())[0]].to_excel(
                os.path.join(tmpdirname, single_filename), index=False
            )
            with open(os.path.join(tmpdirname, single_filename), "rb") as f:
                bytes_data = f.read()
            b64 = base64.b64encode(bytes_data).decode()
            href = f"data:file/xlsx;base64,{b64}"
            st.download_button(
                label="xlsx تحميل الملف بصيغة",
                data=bytes_data,
                file_name=single_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
            )
