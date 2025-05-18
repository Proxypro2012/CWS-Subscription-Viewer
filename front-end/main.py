import time
import streamlit as st
import streamlit.components.v1 as components
import requests
import calendar

# List of months
months = list(calendar.month_name)[1:]

# Page configuration
st.set_page_config(
    layout="wide",
    page_title="CWS Subscription Viewer",
    page_icon="front-end/header-logo.svg",  # Ensure this path is correct
    initial_sidebar_state="expanded"
)

# Base API URL
BASE_URL = "https://cws-subscription-viewer.onrender.com/"

# Layout columns
r1col1, r1col2, r1col3 = st.columns([2, 0.5, 0.5])

# Sidebar
menuOptions = ["Subscription Status", "BlankSite"]
st.sidebar.image("front-end/header-logo.svg")  # Make sure the image path is valid
selected_page = st.sidebar.radio("", options=menuOptions)

# Function to render user status widgets
def spawn_status_widgets(filtered_users):
    for i, user in enumerate(filtered_users):
        with st.status(f"{user['name']}'s Status", expanded=True):
            selected_month = st.selectbox(
                "Select a month", months, key=f"month_select_{user['name']}_{i}"
            )

            # Get years for this subscriber
            url = f"{BASE_URL}/get-subscriber-years?person={user['name']}"
            response = requests.get(url)

            years = []
            if response.status_code == 200:
                data = response.json()
                years = data.get('years', [])

            selected_year = st.selectbox(
                "Select a year", years, key=f"year_select_{user['name']}_{i}"
            )

            st.write(f"You selected: {selected_year}")
            st.write(f"You selected: {selected_month}")

# Main content
if selected_page == "Subscription Status":
    with r1col1:
        st.title("CWS Subscription Status")
    st.divider()

    # Get subscriber list
    response = requests.get(f"{BASE_URL}/get-subscriber-list")
    if response.status_code == 200:
        users = response.json()

        # Search box
        search_query = st.text_input("🔍 Search subscriber").lower().strip()

        # Filter users by name
        filtered_users = [
            user for user in users if search_query in user['name'].lower()
        ] if search_query else users

        st.divider()
        spawn_status_widgets(filtered_users)
    else:
        st.error("Failed to load subscriber list.")
