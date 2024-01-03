import streamlit as st
from streamlit_option_menu import option_menu

from python_pages.app import *
from python_pages.about import *
from python_pages.login import *


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


def valid_function():
    with st.sidebar:
        choos_page = option_menu(
            menu_title="تحليل البيانات و ونظم دعم القرار للإدارة",
            options=["Home", "Photo Editing", "Setting", "About"],
            icons=[
                "house-fill",
                "trophy-fill",
                "gear",
                "info-circle",
            ],
            # menu_icon='chat-text-fill',
            menu_icon="cast",
            default_index=1,
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
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


        if choos_page == "About":
            about_function()
        if choos_page == "Photo Editing":
            functionall()
        # app.functionall()


# if choos_page == "About":
#             # ---------- SIDEBAR ---------- for get html page and set it in side left
#             with open("html/sidebar.html", "r", encoding="UTF-8") as sidebar_file:
#                 sidebar_html = sidebar_file.read().replace("{VERSION}", VERSION)
#             with st.sidebar:
#                 with st.expander("الخدمات التي يقدمها التطبيق"):
#                     st.info(
#                         "* تحميل صورة, ياخذ صورة واحدة من الكاميرا او عبر رابط لصورة \n"
#                         "*  خاصية قص\n"
#                         "* خاصية ابعاد الخلفية\n"
#                         "*خاصية مرآه\n"
#                         "* تحويل الى تدرج رمادي او اسود او ابيض\n"
#                         "* تدوير\n"
#                         "* تغير السطوع, وتشبع اللون, وخاصية التباين, وخاصية حدة اللون\n"
#                         "* توليد صورة عشوائية من مزود الصور\n"
#                         "* تحميل الصورة"
#                     )
#                 st.components.v1.html(sidebar_html, height=500, width=300)
