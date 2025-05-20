import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

# Config
st.set_page_config(page_title="CWS Subscription Viewer")

BASE_URL = "https://cws-subscription-viewer.onrender.com"

# --- Session state defaults ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "home"
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""







# --- Pages ---
def homepage():
    # Centering helper: 3-column layout where the middle column contains all content
    col1, col2, col3 = st.columns([1, 3, 1])

    # Custom CSS for wide buttons (only applies to home page)
    wide_button_css = """
    <style>
    div.stButton > button {
        width: 100%;
        height: 3em;
        font-size: 1.1em;
    }
    </style>
    """
    st.markdown(wide_button_css, unsafe_allow_html=True)

    # Add vertical space
    with col2:
        for i in range(5):
            st.write("")  # Adjust as needed

    with col2:

        # Centered title and text using HTML
        st.markdown("<br><br><br>", unsafe_allow_html=True)  # Vertical space

        # Properly centered title and paragraph with inline style
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <div style="display: inline-flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" height="32px" viewBox="0 -960 960 960" width="32px" fill="#e3e3e3">
                    <path d="M240-200h120v-200q0-17 11.5-28.5T400-440h160q17 0 28.5 11.5T600-400v200h120v-360L480-740 240-560v360Zm-80 0v-360q0-19 8.5-36t23.5-28l240-180q21-16 48-16t48 16l240 180q15 11 23.5 28t8.5 36v360q0 33-23.5 56.5T720-120H560q-17 0-28.5-11.5T520-160v-200h-80v200q0 17-11.5 28.5T400-120H240q-33 0-56.5-23.5T160-200Zm320-270Z"/>
                </svg>
                <span style="font-size: 32px; font-weight: 600; margin-left: 12px; color: #e3e3e3;">Home Page</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<p style="text-align: center;">Welcome to the SBM Website!</p>', unsafe_allow_html=True)



        # Buttons
        if st.button("Login", type="primary", key="home_page"):
            st.session_state.page = "login"
            st.rerun()

        if st.button("Sign Up", type="primary"):
            st.info("Sign up is not implemented yet.")

    # Optional: add visual effect
    try:
        rain('•', 20, falling_speed=5, animation_length="infinite")
    except Exception:
        pass  # in case rain is undefined or external








def login():
    r0col1, r0col2, r0col3 = st.columns([1, 0.5, 1])
    r1col1, r1col2, r1col3 = st.columns([1, 0.5, 1])
    r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
    r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
    r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])

    with r0col2:
        for i in range(10):
            st.write("")

    with r1col2:
        st.title("Login")
    with r2col2:
        username = st.text_input("Username", placeholder="Enter your username")
    with r3col2:
        password = st.text_input("Password", placeholder="Enter your password", type="password")
    with r4col2:
        if st.button("Login", type="primary", key="login_page"):
            creds = {"username": username, "password": password}
            try:
                response = requests.post(f"{BASE_URL}/login", json=creds)
                if response.status_code == 200:
                    st.success("Login successful!")
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.password = password
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Login failed. Please check your credentials.")
            except Exception as e:
                st.error(f"Request failed: {e}")

    rain('•', 20, falling_speed=5, animation_length="infinite")









def dashboard():
    r1col1, r1col2, r1col3 = st.columns([0.25, 4, 0.25])
    r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
    r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])

    

    
    with st.sidebar:
        st.title("Navigation")
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Settings", "Logout"],
            icons=["house", "gear", "box-arrow-right"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

        if selected == "Dashboard":
            st.session_state.page = "dashboard"
            st.rerun()
        elif selected == "Settings":
            st.session_state.page = "settings"
            st.rerun()
       






def settings():
    st.title("Settings")
    st.info("Settings page is under construction.")





# --- Routing ---
if st.session_state.logged_in:
    st.session_state.page = "dashboard"

if st.session_state.page == "home":
    homepage()
elif st.session_state.page == "login":
    login()
elif st.session_state.page == "dashboard":
    dashboard()
elif st.session_state.page == "settings":
    settings()

