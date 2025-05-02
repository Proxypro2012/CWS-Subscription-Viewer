import time
import streamlit as st
import streamlit.components.v1 as components
import requests



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

        for i, user in enumerate(users):
            with st.status(f"{user['name']}'s Status", expanded=True):
                st.write(f"📄 Status: {user['status']}")
                st.write(f"📅 Expires: {user['expires']}")
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
    for i in range(10):
        st.write("")
    spawn_status_widgets()






