# import streamlit as st
# from python_pages.connect_database import *


# def info_table_function():
#     placeholder = st.empty()



#     # Insert a form in the container
#     with placeholder.form("login"):
#         st.markdown("##### إنشاء اتصال مع قاعدة البيانات")
#         table_name = st.text_input("Table Name")
#         # user_name = st.text_input("condati")

#         submit = st.form_submit_button("استعلام")

#         # send data to check in database_connect

#         if table_name == "":
#             st.error("البيانات لاتزال فارغة")
#         elif submit and table_name != "":
#             st.success("قيد  الاستعلام")
#             if choose_table(tableName=table_name) == True:
#                 st.success("تم الاستعلام  بنجاح")

#         elif submit and table_name == "":
#             st.error("فشل في الاستعلام من قاعدة البيانات")
#         else:
#             st.error("فشل في الاستعلام مع قاعدة البيانات")
