import streamlit as st
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('<hostname>', '<port>', service_name='<service_name>')
conn = cx_Oracle.connect(user='<username>', password='<password>', dsn=dsn_tns)

def fetch_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    cursor.close()
    return data

def main():
    st.title('Oracle Data Viewer')
    data = fetch_data()
    st.table(data)
if __name__ == '__main__':
    main()
