import mysql.connector
import streamlit as st
import pandas as pd


def connect_database(host_name, user_name, pass_name, database_name, table_name):
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=pass_name,
        database=database_name,
    )
    
    
    t_name = table_name
    
    if t_name == "users":
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
            st.title(" connect python and mysql")
            df = pd.DataFrame(data, columns=cursor.column_names)
            st.dataframe(df)
    elif t_name == "carts":
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM carts")
            data = cursor.fetchall()
            st.title(" connect python and mysql")
            df = pd.DataFrame(data, columns=cursor.column_names)
            st.dataframe(df)
    elif t_name == "brands":
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM brands")
            data = cursor.fetchall()
            st.title(" connect python and mysql")
            df = pd.DataFrame(data, columns=cursor.column_names)
            st.dataframe(df) 
    elif t_name == "products":
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products")
            data = cursor.fetchall()
            st.title(" connect python and mysql")
            df = pd.DataFrame(data, columns=cursor.column_names)
            st.dataframe(df)   
    elif t_name == "colors":
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM colors")
            data = cursor.fetchall()
            st.title(" connect python and mysql")
            df = pd.DataFrame(data, columns=cursor.column_names)
            st.dataframe(df)  


# connection = mysql.connector.connect(
#     host="localhost", user="root", password="", database="webecommerce"
# )
# cursor = connection.cursor()

# # step 1
# # cursor = connection.cursor()
# # cursor.execute("SELECT * FROM users")
# # print(cursor.fetchall())

# # step 2
# # cursor = connection.cursor()
# # cursor.execute("SELECT * FROM users")
# # data = cursor.fetchall()
# # st.title("firas connect python and laravel")
# # df = pd.DataFrame(data, columns=cursor.column_names)
# # st.dataframe(df)


# cursor.execute("SELECT users.name FROM users  WHERE users.name = 'admin'")


# data = cursor.fetchall()

# # st.title("firas connect python and laravel")
# # df = pd.DataFrame(data, columns=cursor.column_names)
# # st.dataframe(df)
