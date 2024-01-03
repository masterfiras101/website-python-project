# import streamlit_authenticator as stauth

# # st.set_page_config(
# #     page_title="صفحة تسجيل الدخول",
# # )
# VERSION = "0.7.0"


# login_form = """
#     <body>
#         <h2 id="title-form-login">صفحة تسجيل الدخول من فضلك قم بتسجيل الدخول أولاّ </h2>
#         <form id="login-form">
#             <label for="uname"><b>إسم المستخدم</b></label>
#             <input type="text" id="c-name"placeholder="ادخل اسم المستخدم هنا" name="uname" required>
#             <label for="psw"><b>كلمة المرور</b></label>
#             <input type="password" id="c-pass" placeholder="ادخل كلمة المرور هنا" name="psw" required>
#             <input type="submit" value="دخول">
#         </form>
#     </body>
# """


# st.markdown(login_form, unsafe_allow_html=True)


# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# local_css("css/login-style.css")


# Create an empty container
import streamlit as st

# from true_valid import *


def login_function():
    placeholder = st.empty()

    actual_email = "u"
    actual_password = "p"

    # u = connect_database.data

    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("##### تسجيل الدخول")
        email = st.text_input("الايميل")
        password = st.text_input("كلمة المرور", type="password")
        submit = st.form_submit_button("دخول")
        # send data to check in database_connect
        # if submit is not None :
        #     def check_true(email,):
        if submit and email == actual_email and password == actual_password:
            # placeholder.empty()
            st.success("تم تسجيل الدخول بنجاح")
        elif submit and email != actual_email and password != actual_password:
            st.error("فشل في تسجيل الدخول يرجى مراجعة المسؤول")
        else:
            pass
