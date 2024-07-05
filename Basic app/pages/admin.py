import time

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from menu import menu_ui

with open("user.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

menu_ui()

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)


def yaml_update():
    with open("user.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)


def temp_button(usr: str):
    st.write(f"Hello {usr}!")
    st.write(config["credentials"]["usernames"][i])


def delete_button(usr: str):
    global config
    del config["credentials"]["usernames"][usr]
    with open("user.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)
    with open("user.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)
    st.write(f"Deleted {usr}.")


def make_admin_button(username: str):
    global config
    config["credentials"]["usernames"][username]["admin"] = True
    with open("user.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)
    with open("user.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)
    st.write(f"Made {username} admin.")


def unmake_admin_button(username: str):
    global config
    config["credentials"]["usernames"][username]["admin"] = False
    with open("user.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)
    with open("user.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)
    st.write(f"Unmade {username} admin.")


if "admin" not in st.session_state:
    st.switch_page("pages/login.py")
elif st.session_state["admin"] is False:
    st.switch_page("Home.py")
else:
    st.title("Wassup admin baby.")
    for i in config["credentials"]["usernames"]:
        if i == st.session_state["username"]:
            continue
        with st.expander(i):
            if st.button(i):
                temp_button(i)
            if (
                    "admin" in config["credentials"]["usernames"][i]
                    and config["credentials"]["usernames"][i]["admin"] is True
            ):
                if st.button(f"Unmake {i} admin?"):
                    unmake_admin_button(i)
                    time.sleep(2.5)
                    st.rerun()
            else:
                if st.button(f"Make {i} admin?"):
                    make_admin_button(i)
                    time.sleep(2.5)
                    st.rerun()
            if st.button(f"Delete {i}"):
                delete_button(i)
                time.sleep(2)
                st.rerun()
    if st.button("Register new User"):
        st.switch_page("pages/register_user.py")
