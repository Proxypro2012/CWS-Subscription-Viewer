import time
import streamlit as st
import streamlit.components.v1 as components
import requests
import calendar


months = list(calendar.month_name)[1:]


st.set_page_config(
    layout="wide",
    page_title="CWS Subscription Viewer",
    page_icon="front-end/header-logo.svg",  # Optionally, set a page icon
    initial_sidebar_state="expanded"
)

BASE_URL = "https://cws-subscription-viewer.onrender.com/"

r1col1, r1col2, r1col3 = st.columns([2, 0.5, 0.5])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 2, 1])
r4col1, r4col2, r4col3 = st.columns([1, 2, 1])
r5col1, r5col2, r5col3 = st.columns([1, 2, 1])



def spawn_status_widgets():
    url = f"{BASE_URL}/get-subscriber-list"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        # Show status widgets for each filtered user
        for i, user in enumerate(filtered_users):
            with st.status(f"{user['name']}'s Status", expanded=True):
                selected_month = st.selectbox(
                    "Select a month", months, key=f"month_select_{user['name']}_{i}"
                )

                years = str(f"{BASE_URL}/get-subscriber-years?person={user['name']}").get('years')
        
                selected_year = st.selectbox("Select a year", years, key=f"year_select_{user['name']}_{i}")
                st.write(f"You selected: {selected_year}")
                st.write(f"You selected: {selected_month}")
                
    else:
        st.error("Failed to load subscriber list.")




# Sidebar 
menuOptions = []
#st.sidebar.title("Navigation")
st.sidebar.image("front-end/header-logo.svg")
menuOptions.extend(["Subscription Status", "BlankSite"])
selected_page = st.sidebar.radio("", options=menuOptions)






if selected_page == menuOptions[0]:
    with r1col1:
      st.title("Subscription Status")
    st.divider()

    url = f"{BASE_URL}/get-subscriber-list"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()


    search_query = st.text_input("🔍 Search subscriber").lower().strip()

        # Filter users by name
    filtered_users = [
            user for user in users if search_query in user['name'].lower()
    ] if search_query else users

    st.divider()


    for i in range(10):
        st.write("")
    spawn_status_widgets()






