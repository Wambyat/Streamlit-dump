import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from menu import menu_ui

menu_ui()

with open("user.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

if (
        "authentication_status" in st.session_state
        and st.session_state["authentication_status"] is True
):
    if (
            "admin" in config["credentials"]["usernames"][st.session_state["username"]]
            and config["credentials"]["usernames"][st.session_state["username"]]["admin"]
            is True
    ):
        st.session_state["admin"] = True
    st.write("Go home???")
    st.switch_page("Home.py")
else:
    if st.session_state["logout"] is None:
        st.session_state["logout"] = True
    authenticator.login()
    if st.session_state["authentication_status"] is False:
        st.error("Login failed. Username and password do not match.")
