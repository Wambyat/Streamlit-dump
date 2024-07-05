import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


def admin_menu():
    st.sidebar.page_link("pages/admin.py", label="Manage users")


def regular_menu():
    with st.sidebar:
        st.page_link("Home.py", label="Home")
        st.page_link("pages/update_user.py", label="Your profile")
        if st.button("Reset Password"):
            st.switch_page("pages/reset_password.py")
        if st.button("Logout"):
            with open("user.yaml") as file:
                config = yaml.load(file, Loader=SafeLoader)
            authenticator = stauth.Authenticate(
                config["credentials"],
                config["cookie"]["name"],
                config["cookie"]["key"],
                config["cookie"]["expiry_days"],
            )
            st.session_state["admin"] = False
            authenticator.authentication_handler.execute_logout()
            st.switch_page("pages/login.py")


def logged_out_menu():
    st.sidebar.page_link("pages/login.py", label="Log in")


def menu_ui():
    if "authentication_status" not in st.session_state or st.session_state[
        "authentication_status"
    ] in [False, None]:
        logged_out_menu()
        return
    elif "admin" in st.session_state and st.session_state["admin"] is True:
        admin_menu()
    regular_menu()
