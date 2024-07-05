import streamlit as st


# This file is here to supress warnings from IDEs. It is not actually used.


def admin_menu():
    st.sidebar.page_link("pages/admin.py", label="Manage users")


def regular_menu():
    st.sidebar.page_link("Home.py", label="Home")
    st.sidebar.page_link("pages/update_user.py", label="Your profile")


def logged_out_menu():
    st.sidebar.page_link("pages/login.py", label="Log in")


def menu_ui():
    if "authentication_status" not in st.session_state:
        logged_out_menu()
        return
    elif "admin" in st.session_state and st.session_state["admin"] is True:
        admin_menu()
    regular_menu()
