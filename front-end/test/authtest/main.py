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



# Function to display login page
def login_page():
    st.title("Login Page")
    
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")
    
    if st.button("Login"):
        creds = {"username": username, "password": password}
        response = requests.post(f"{BASE_URL}/login", json=creds)
        
        if response.status_code == 200:
            st.session_state.logged_in = True
            st.session_state.org_name = username  # Storing the organization name in session
            st.success("Login successful!")
            # No need to rerun, the app will automatically switch to dashboard
        else:
            st.error("Login failed. Please check your credentials.")

# Function to display dashboard page after successful login
def dashboard_page():
    st.title(f"Welcome to {st.session_state.org_name}'s Dashboard")
    
    # Add a line below the title
    st.write("---")
    
    # You can add more dashboard content here related to the organization
    st.write(f"Welcome to {st.session_state.org_name}'s dashboard!")
    
    # Example of displaying some additional data or subscription status here:
    # st.write("Subscription details can go here...")

    # Trigger the rain effect on the page
    rain('•', 20, falling_speed=5, animation_length="infinite")


# Check the login status and display the appropriate page
if st.session_state.logged_in:
    # Show the dashboard page if logged in
    dashboard_page()
else:
    # Show login page if not logged in
    login_page()