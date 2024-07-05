import time

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

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
        and "admin" in st.session_state
        and st.session_state["admin"] is True
):
    try:
        email, username, name = authenticator.register_user(pre_authorization=False)
        if email:
            st.success(f"Registration successful. Email: {email}")
            with st.spinner("Redirecting to login page..."):
                yaml_update()
                time.sleep(2)
                st.session_state["admin"] = False
                authenticator.authentication_handler.execute_logout()
                st.switch_page("pages/login.py")
    except Exception as e:
        st.error(e)
else:
    st.switch_page("Home.py")

if st.button("Go back"):
    st.switch_page("pages/admin.py")
