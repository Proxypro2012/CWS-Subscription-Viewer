import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain

# Page configuration
st.set_page_config(page_title="CWS Subscription Viewer")

BASE_URL = "https://cws-subscription-viewer.onrender.com"

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "org_name" not in st.session_state:
    st.session_state.org_name = ""

# Layout columns for your original design
r1col1, r1col2, r1col3 = st.columns([1, 0.5, 1])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])


# Function to display login page
def login_page(r1col2, r2col2, r3col2, r4col2):
    with r1col2:
        st.title("Login")
    with r2col2:
        username = st.text_input("Username", placeholder="Enter your username")
    with r3col2:
        password = st.text_input("Password", placeholder="Enter your password", type="password")
    with r4col2:
        if st.button("Login", type="primary"):
            creds = {"username": username, "password": password}
            response = requests.post(f"{BASE_URL}/login", json=creds)
            
            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.org_name = username  # Store organization name in session state
                st.success("Login successful!")
                st.experimental_rerun()  # Automatically rerun to switch to dashboard
            else:
                st.error("Login failed. Please check your credentials.")

# Function to display dashboard page after successful login
def dashboard_page():
    with r1col2:
        st.title(f"Welcome to {st.session_state.org_name}'s Dashboard")
    with r2col2:
        st.write("---")  # A line under the title
    with r3col2:
        # You can add more dashboard content here, for example, subscription details or user info
        st.write(f"Welcome to {st.session_state.org_name}'s dashboard!")
    
    # Example of displaying subscription or user-related data
    # st.write("Subscription details can go here...")

    # Trigger the rain effect on the page
    rain('•', 20, falling_speed=5, animation_length="infinite")

    # Add a logout button in the dashboard
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.org_name = ""
        st.experimental_rerun()  # Optional: Reload the app to show the login page again


# Main layout: Show login page if not logged in or dashboard page if logged in
if not st.session_state.logged_in:
    # Show login page if not logged in
    login_page(r1col2, r2col2, r3col2, r4col2)
else:
    # Show dashboard page if logged in
    dashboard_page()