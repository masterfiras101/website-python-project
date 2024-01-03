import streamlit as st
from python_pages.connect_database import *
from python_pages.infodatatablefromdatabase import *


def info_database_function():
    placeholder = st.empty()

    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("##### إنشاء اتصال مع قاعدة البيانات")
        host_name = st.text_input("Host Name")
        user_name = st.text_input("Username")
        pass_name = st.text_input("Password")
        database_name = st.text_input("Database Name")
        table_name = st.text_input("Table Name")

        submit = st.form_submit_button("اتصال")

        # send data to check in database_connect

        if (
            host_name == ""
            and user_name == ""
            and pass_name == ""
            and database_name == ""
            and table_name == ""
        ):
            st.error("البيانات لاتزال فارغة")
        elif (
            submit
            and host_name != ""
            and user_name != ""
            and database_name != ""
            and table_name != ""
        ):
            connect_database(
                    host_name=host_name,
                    user_name=user_name,
                    pass_name=pass_name,
                    database_name=database_name,
                    table_name=table_name,
                )
            st.success("تم الاتصال مع قاعدة البانات بنجاح")

        elif (
            submit
            and user_name != ""
            or host_name != ""
            or database_name != ""
            or table_name != ""
        ):
            st.error("فشل في الاتصال مع قاعدة البيانات")
        else:
            st.error("فشل في الاتصال مع قاعدة البيانات")

        # elif submit and host_name == "" and user_name == "" and database_name == "":


#     def check_true(email,):
# if submit and email == actual_email and password == actual_password:
#     # placeholder.empty()
#     st.success("تم تسجيل الدخول بنجاح")
# elif submit and email != actual_email and password != actual_password:
#     st.error("فشل في تسجيل الدخول يرجى مراجعة المسؤول")
# else:
#     pass
