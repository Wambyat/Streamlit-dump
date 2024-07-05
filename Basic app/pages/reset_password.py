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

st.title("Change your password")

if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success("Password modified successfully")
            with open("user.yaml", "w") as file:
                yaml.dump(config, file)
    except Exception as e:
        st.error(e)
else:
    st.switch_page("pages/login.py")
