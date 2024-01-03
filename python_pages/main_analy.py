import streamlit as st
import pandas as pd
import plotly.express as px




def main_analy():
    # add title for the app

    st.title("اكتشاف وتحليل البيانات")

    # sidebar title
    st.title("CSV قم بتحميل الملف بصيغة")

    # add file-uploader widget
    uploaded_data = st.file_uploader("CSV صيغة ")

    # add tabs
    tab1, tab2, tab3 = st.tabs(
        ["معلومات عامة عن البيانات", "ميزات مع الرسوم البيانية", "ميزات نهائية"]
    )

    @st.cache_data
    def load_data(file_name):
        # read CSV file
        data = pd.read_csv(file_name)
        return data

    if uploaded_data is not None:
        # read csv
        df = load_data(uploaded_data)

    with tab1:
        if uploaded_data is not None:
            # extract meta-data from the uploaded dataset
            st.header("وصف البيانات")

            row_count = df.shape[0]

            column_count = df.shape[1]

            # Use the duplicated() function to identify duplicate rows
            duplicates = df[df.duplicated()]
            duplicate_row_count = duplicates.shape[0]

            missing_value_row_count = df[df.isna().any(axis=1)].shape[0]

            table_markdown = f"""
        | Description | Value | 
        |---|---|
        | Number of Rows | {row_count} |
        | Number of Columns | {column_count} |
        | Number of Duplicated Rows | {duplicate_row_count} |
        | Number of Rows with Missing Values | {missing_value_row_count} |
        """

            st.markdown(table_markdown)

            st.header("انواع الاعمدة")
            st.header(" بالتاشير على جدول البيانات csv قم بحفظ البيانات بصيغة ")

            # get feature names
            columns = list(df.columns)

            # create dataframe
            column_info_table = pd.DataFrame(
                {"العمود": columns, "نوع البانات": df.dtypes.tolist()}
            )

            # display pandas dataframe as a table
            st.dataframe(column_info_table, hide_index=True)
            with tab2:
                if uploaded_data is not None:
                    # find numeric features  in the dataframe
                    numeric_cols = df.select_dtypes(include="number").columns.tolist()
            with tab2:
                if uploaded_data is not None:
                    # find numeric features  in the dataframe
                    numeric_cols = df.select_dtypes(include="number").columns.tolist()

                    # add selection-box widget
                    selected_num_col = st.selectbox(
                        "Which numeric column do you want to explore?", numeric_cols
                    )

                    st.header(f"{selected_num_col} - Statistics")

                    col_info = {}
                    col_info["Number of Unique Values"] = len(
                        df[selected_num_col].unique()
                    )
                    col_info["Number of Rows with Missing Values"] = (
                        df[selected_num_col].isnull().sum()
                    )
                    col_info["Number of Rows with 0"] = df[selected_num_col].eq(0).sum()
                    col_info["Number of Rows with Negative Values"] = (
                        df[selected_num_col].lt(0).sum()
                    )
                    col_info["Average Value"] = df[selected_num_col].mean()
                    col_info["Standard Deviation Value"] = df[selected_num_col].std()
                    col_info["Minimum Value"] = df[selected_num_col].min()
                    col_info["Maximum Value"] = df[selected_num_col].max()
                    col_info["Median Value"] = df[selected_num_col].median()

                    info_df = pd.DataFrame(
                        list(col_info.items()), columns=["Description", "Value"]
                    )

                    # display dataframe as a markdown table
                    st.dataframe(info_df)

                    st.header("الرسوم البيانية")
                    fig = px.histogram(df, x=selected_num_col)
                    st.plotly_chart(fig, use_container_width=True)
                    with tab3:
                        if uploaded_data is not None:
                            # find categorical columns in the dataframe
                            cat_cols = df.select_dtypes(include="object")
                            cat_cols_names = cat_cols.columns.tolist()

                            # add select widget
                            selected_cat_col = st.selectbox(
                                "Which text column do you want to explore?",
                                cat_cols_names,
                            )

                            st.header(f"{selected_cat_col}")

                            # add categorical column stats
                            cat_col_info = {}
                            cat_col_info["Number of Unique Values"] = len(
                                df[selected_cat_col].unique()
                            )
                            cat_col_info["Number of Rows with Missing Values"] = (
                                df[selected_cat_col].isnull().sum()
                            )
                            cat_col_info["Number of Empty Rows"] = (
                                df[selected_cat_col].eq("").sum()
                            )
                            cat_col_info["Number of Rows with Only Whitespace"] = len(
                                df[selected_cat_col][df[selected_cat_col].str.isspace()]
                            )
                            cat_col_info["Number of Rows with Only Lowercases"] = len(
                                df[selected_cat_col][df[selected_cat_col].str.islower()]
                            )
                            cat_col_info["Number of Rows with Only Uppercases"] = len(
                                df[selected_cat_col][df[selected_cat_col].str.isupper()]
                            )
                            cat_col_info["Number of Rows with Only Alphabet"] = len(
                                df[selected_cat_col][df[selected_cat_col].str.isalpha()]
                            )
                            cat_col_info["Number of Rows with Only Digits"] = len(
                                df[selected_cat_col][df[selected_cat_col].str.isdigit()]
                            )
                            cat_col_info["Mode Value"] = df[selected_cat_col].mode()[0]

                            cat_info_df = pd.DataFrame(
                                list(cat_col_info.items()),
                                columns=["Description", "Value"],
                            )
                            st.dataframe(cat_info_df)
