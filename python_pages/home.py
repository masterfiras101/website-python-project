
import streamlit as st
import pandas as pd
import plotly.express as px  # pip install plotly-express 
import base64
from io import StringIO, BytesIO


# this function for download Excel File from link 

# def generate_excel_download_link(df):
#     towrite = BytesIO()
#     df.to_excel(towrite, encoding="utf-8", index=False, header=True) 
#     towrite.seek(0)
#     b64 = base64.b64encode(towrite.read()).decode()
#     href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx"> Downloade Excel File.. </a>'
#     return st.markdown(href, unsafe_allow_html=True)


def analy_xlsx():


# this function for download the chart of data in Extension html File from link 

    def generate_html_download_link(fig):
        towrite = StringIO()
        fig.write_html(towrite, include_plotlyjs="cdn")
        towrite = BytesIO(towrite.getvalue().encode())
        b64 = base64.b64encode(towrite.read()).decode()
        href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download ="plot.html">تحميل الرسم البياني للبيانات</a>'
        return st.markdown(href,unsafe_allow_html=True)

    # st.set_page_config(
    #     page_title="صفحة تحليل البيانات",
    #     page_icon="📊",
    # )

    st.title(" CSV تحليل ملفات الاكسل وحفظها بصيغة ")

    uploade_file = st.file_uploader('اختر ملف الاكسل من الجهاز', type='xlsx')

    if uploade_file :
        st.markdown('---')
        df = pd.read_excel(uploade_file, engine='openpyxl')
        st.dataframe(df)
        groupby_column = st.selectbox(
            'اختر العمود المراد البحث عنه ؟',
            ('id','name')
        )
        
        output_columns = [
            'age',
            'level'
        ]
        df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
        st.dataframe(df_grouped)
        
        fig = px.bar(
            df_grouped,
            x = groupby_column,
            y='age',
            color='level',
            color_continuous_scale =['red', 'yellow', 'green'],
            template='plotly_white',
            title=f'<b>Age & Level by {groupby_column}</b>'
        )
        st.plotly_chart(fig)
        
        st.subheader(": اختر نوع التحميل")
        # generate_excel_download_link(df_grouped)
        generate_html_download_link(fig)