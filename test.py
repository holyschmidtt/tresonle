import streamlit as st
import numpy as np

def main():

    menu = ["Home", "Login", "Sign-Up"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.title("ACO")
        st.subheader("Dean baka naman, #tresonle Xd")

    elif choice == "Login":
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')


if __name__ == '__main__':
    main()
