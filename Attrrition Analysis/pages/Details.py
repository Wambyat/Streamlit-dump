import random

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Attrition Solver",
    page_icon="shark",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/wambyat/AttritionAnalysisSE',
        'Report a bug': "https://github.com/wambyat/AttritionAnalysisSE",
        'About': "This application will figure out which of your employees are most likely to leave. It can also tell you why and suggest a few basic solutions. Call 1800-this-a-proj for addition help"
    }
)

# Initializing all the session_state variables
# This is technically a leftover
# reused to track which solutions have been chosen
if 'page' not in st.session_state:
    st.session_state['page'] = {}

# This is technically a leftover
# Reused to track which employee is selected
if 'inp' not in st.session_state:
    st.session_state['inp'] = 'default'

# This is used to track if the user has logged in
if 'login' not in st.session_state:
    st.session_state['login'] = 'No'

# This is used to track if the input is given.
if 'input' not in st.session_state:
    st.session_state['input'] = 'No'

# This is also used to track user login
# TODO Merge this and 'login'
if 'login_test' not in st.session_state:
    st.session_state['login_test'] = 0

if 'model' not in st.session_state:
    st.session_state['model'] = 'No'

if st.session_state['login'] == 'No':

    st.title("Please go to login page and login first!")

elif st.session_state['model'] == 'No':
    st.title("Please give an input and run the model.")
    st.subheader("Navigate to the input page to do this.")

else:

    st.title("Name: Lorem Ipsum")

    a = random.randint(1, 5)
    col1, col2 = st.columns(2)
    mapping = {1: ["Intense Workload", "Lessen the workload"],
               2: ["No clear Understanding and weak ManagerRelationship", "Training Enhancement"],
               3: ["Less Projects than Usual", "Urgent Counselling and Affirmation of value forEmployee to be shown"],
               4: ["Project Workload",
                   "Balancing of Projects by reducing the number of projects in accordance to the number of work hours"],
               5: ["Working for long hours", "Incentives ++"],
               6: ["Recently entering the seniority zone with more projects", "More Mentoring"]
               }

    img = Image.open(str(a) + ".jpg")
    c = st.container()

    with c:

        temp_dict = st.session_state['page']

        with col1:

            st.image(img)

            df_t = st.session_state['model_res'][st.session_state['model_res']['Emp_ID'] == st.session_state['inp']]

            st.metric("Customer Satisfaction", str(int(df_t['satisfaction_level'] * 100)) + "%")
            st.metric("Last Evaluation", str(int(df_t['last_evaluation'] * 100)) + "%")
            st.write("Number of projects: " + str(int(df_t['number_project'])))
            st.write("Hours per month: " + str(int(df_t['average_monthly_hours'])))
            st.write("Years with your company: " + str(int(df_t['time_spend_company'])))
            st.write("Recent promotion: " + str("Yes" if int(df_t['promotion_last_5years']) == 1 else "No"))
            st.write("Department: " + str(int(df_t['Departments '])))
            st.write("Salary: " + str(int(df_t['salary'])))

        with col2:

            df = st.session_state['model_res']

            for index, row in df.iterrows():

                if row["Emp_ID"] == st.session_state['inp']:

                    string = "Odds: " + str(int((row['odds']) * 100)) + "%"
                    st.subheader(string)
                    st.subheader("Reasons:")
                    lst = []

                    for i in row['reason']:
                        lst.append(mapping[i][0])

                    for i in lst:
                        st.markdown("* " + i)

                    st.subheader("Solutions:")
                    lst2 = []

                    for i in row['reason']:
                        lst2.append(mapping[i][1])

                    for i in lst2:

                        a = st.checkbox(str(i), key=str(i))

                        if a:

                            if row["Emp_ID"] not in temp_dict.keys():

                                temp_dict[row["Emp_ID"]] = [str(i)]

                            else:

                                if str(i) not in temp_dict[row["Emp_ID"]]:
                                    temp_dict[row["Emp_ID"]].append(str(i))

    st.session_state['page'] = temp_dict
