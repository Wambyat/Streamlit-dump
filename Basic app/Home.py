import subprocess

import streamlit as st

from menu import menu_ui

menu_ui()


# Output comes above everything else, can be changed by doing session_state shenanigans
def script_run(name, age):
    result = subprocess.run(["python", "demo_script.py", name, str(age)])
    st.write(result)


if (
        "authentication_status" in st.session_state
        and st.session_state["authentication_status"] is True
):
    st.title("Wassup this home page.")
    if st.button("Click for script"):
        with st.form(key="my_form"):
            name = st.text_input("Name", value="John Doe")
            age = st.number_input("Age", min_value=0, max_value=100, value=1)
            submitted = st.form_submit_button(
                "Submit", on_click=script_run, args=(name, age)
            )
else:
    st.switch_page("pages/login.py")
