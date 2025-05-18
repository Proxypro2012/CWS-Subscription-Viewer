import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain
from streamlit_navigation_bar import st_navbar

# Page configuration
st.set_page_config(page_title="CWS Subscription Viewer")

BASE_URL = "https://cws-subscription-viewer.onrender.com"


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



def login():
    # UI Layout
    r1col1, r1col2, r1col3 = st.columns([1, 0.5, 1])
    r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
    r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
    r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])

    for i in range(5):
        st.write("")

    with r1col2:
        st.title("Login")

    with r2col2:
        username = st.text_input("Username", placeholder="Enter your username")
    with r3col2:
        password = st.text_input("Password", placeholder="Enter your password", type="password")

    with r4col2:
        if st.button("Login", type="primary"):
            creds = {"username": username, "password": password}
            
            try:
                response = requests.post(f"{BASE_URL}/login", json=creds)
                # st.write(f"Response status: {response.status_code}")
                # st.write(response.text)  # Show full response for debugging

                if response.status_code == 200:
                    st.success("Login successful!")
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.password = password
                else:
                    st.error("Login failed. Please check your credentials.")
            except Exception as e:
                st.error(f"Request failed: {e}")


    # Trigger the rain
    rain('•', 20, falling_speed=5, animation_length="infinite")


def dashboard():
    r1col1, r1col2, r1col3 = st.columns([0.25, 4, 0.25])
    r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
    r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
    r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])

    with r1col2:
        st.title("Dashboard")
    with r2col2:
        st.divider()
        
        


def homepage():
    r1col1, r1col2, r1col3 = st.columns([0.25, 4, 0.25])
    r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
    r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
    r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])

    with r1col2:
        st.title("Home Page")
    with r2col2:
        st.divider()
        st.write("Welcome to the SBM Website!")
    with r3col2:
        if st.button("Login", type="primary"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.password = ""
            st.experimental_rerun()
    with r4col2:
        if st.button("Sign Up", type="primary"):
            pass
        
if not st.session_state.logged_in:
    # Show login page if not logged in
    login()
else:
    # Show dashboard page if logged in
    dashboard()