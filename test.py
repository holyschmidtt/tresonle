import streamlit as st
import hashlib
import streamlit.components.v1 as components
from PIL import Image
from pathlib import Path
import sqlite3 
import numpy as np

conn = sqlite3.connect('user.db')
c = conn.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def main():

    menu = ["Home", "Login", "Sign-Up"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.title("ACO")
        st.subheader("Dean baka naman, #tresonle Xd")

    elif choice == "Login":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:

                st.sidebar.success("Logged In as {}".format(username))
                task = ["Catalogue", "Contact"]
                task1 = st.selectbox("Menu",task)

                if task1 == "Catalogue":
                    t1 = st.selectbox("Category",["Casual","Classic","Street"])

                    if t1 == "Casual":
                        col1,col2,col3 = st.beta_columns(3)
                        col1.image("1.jpg")
                        col2.image("2.jpg")
                        col3.image("3.jpg")

                    elif t1 == "Classic":
                        col4,col5,col6 = st.beta_columns(3)
                        col4.image("4.jpg")
                        col5.image("5.jpg")
                        col6.image("6.jpg")

                    elif t1 == "Street":
                        col7,col8,col9 = st.beta_columns(3)
                        col7.image("7.jpg")
                        col8.image("8.jpg")
                        col9.image("9.jpg")
                    

    elif choice == "Sign-Up":
        st.subheader("Create New Account")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")



if __name__ == '__main__':
    main()