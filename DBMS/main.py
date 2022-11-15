import streamlit as st
import mysql.connector

db_name = "proj"
db=mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "password",
    database = db_name

)
cursor=db.cursor()

st.write("DBMS Proj")

with st.form("SQL Input"):

    sql = st.text_input("SQL Statement").lower()
    submitted = st.form_submit_button("Submit")


login_check = 0

if submitted:

    cursor.execute(sql)
    login_table = []

    for i in cursor.fetchall():

        st.code(i)

else:

    print("c")