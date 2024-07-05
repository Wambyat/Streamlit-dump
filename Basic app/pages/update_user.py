import time

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator import UpdateError
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


def yaml_update():
    with open("user.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)


if (
        "authentication_status" in st.session_state
        and st.session_state["authentication_status"] is True
):
    st.title("Wassup this profile page.")
    st.write(f"Username: {st.session_state['username']}")
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success("User details updated successfully.")
            yaml_update()
            time.sleep(2.5)
            st.rerun()
    except UpdateError as e:
        st.error(e)
else:
    st.switch_page("pages/login.py")
