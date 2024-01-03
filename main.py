import streamlit as st
from streamlit_option_menu import option_menu

from python_pages.login import *
from python_pages.about import *
from python_pages.app import *
from python_pages.home import *
from python_pages.main_analy import *
from python_pages.convert_csv_to_xlsx import *
from python_pages.infodatabase import *


# st.set_page_config(
#     page_title="الصفحةالرئيسية",
# )


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append(
            {
                "title": title,
                "function": function,
            }
        )


VERSION = "0.7.0"


def run():
    with st.sidebar:
        choos_page = option_menu(
            menu_title="تحليل البيانات والمساعدة في دعم القرار للإدارة",
            options=[
                "CSV تحليل ملفات بصيغة",
                "Xlsx تحليل ملفات بصيغة",
                "xlsx الى  csv تحويل من ",
                "اتصال مع قواعد البيانات",
                "حول المطورين",
            ],
            icons=[
                "house-fill",
                "trophy-fill",
                "gear",
                "gear",
                "info-circle",
            ],
            # menu_icon='chat-text-fill',
            menu_icon="cast",
            default_index=1,
            styles={
                "container": {"padding": "important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {
                    "color": "white",
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                },
                "nav-link-selected": {"background-color": "#009fe8"},
            },
        )

    if choos_page == "Xlsx تحليل ملفات بصيغة":
        analy_xlsx()
    if choos_page == "CSV تحليل ملفات بصيغة":
        main_analy()
    if choos_page == "xlsx الى  csv تحويل من ":
        converCsv()
    if choos_page == "اتصال مع قواعد البيانات":
        info_database_function()
    if choos_page == "حول المطورين":
        about_function()
    # if choos_page == "تعديل الصور":
    #     functionall()


run()
