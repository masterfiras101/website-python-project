# import pandas as pd
# import streamlit as st
# import plotly.express as px


# # Write the code for the Streamlit app
# def write():
#     st.title("Ecommerce Monthly Sales Analysis")
#     uploaded_file = st.file_uploader(
#         "Upload your sales data as a CSV file", type=["csv"]
#     )
#     if uploaded_file is not None:
#         sales_data = pd.read_csv(uploaded_file)

#         # Clean and transform the data
#         sales_data.dropna(inplace=True)
#         sales_data["date"] = pd.to_datetime(sales_data["date"])
#         sales_data["month"] = sales_data["date"].dt.month

#         # Aggregate the data by month
#         monthly_sales = sales_data.groupby(["month"], as_index=False).sum()

#         st.write("This is a dashboard showing the aggregated sales data by month.")

#         # Line chart of total sales by month
#         st.write("Line chart of total sales by month:")
#         st.write(px.line(monthly_sales, x="month", y="sales"))

#         # Bar chart of total sales by product
#         st.write("Bar chart of total sales by product:")
#         product_sales = sales_data.groupby(["product"], as_index=False).sum()
#         st.bar_chart(product_sales)

#         # Pie chart of sales by region
#         st.write("Pie chart of sales by region:")
#         region_sales = sales_data.groupby(["region"], as_index=False).sum()
#         st.write(px.pie(region_sales, values="sales", names="region"))

#         # Histogram of product sales by month name
#         st.write("Histogram of product sales by month name:")
#         product_monthly_sales = sales_data.groupby(
#             ["product", "month"], as_index=False
#         ).sum()
#         st.write(
#             px.histogram(product_monthly_sales, x="month", y="sales", color="product")
#         )


# # Deploy the app
# if __name__ == "__main__":
#     write()

# =====================

