import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain
from googletrans import Translator

# Config
st.set_page_config(page_title="CWS Subscription Viewer")

BASE_URL = "https://cws-subscription-viewer.onrender.com"

# --- Translator Setup ---
translator = Translator()

# --- Session State Defaults ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "home"
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""
if "language" not in st.session_state:
    st.session_state.language = "en"  # default language

# --- Translation Helpers ---
@st.cache_data(show_spinner=False)
def safe_translate(text, lang):
    if lang == "en":
        return text
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception:
        return text  # fallback

def translate(text):
    translated = safe_translate(text, st.session_state.language)
    return translated.strip() if translated.strip() else text

# --- Pages ---
def homepage():
    col1, col2, col3 = st.columns([1, 3, 1])
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

    with col2:
        for _ in range(5):
            st.write("")

        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <div style="display: inline-flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" height="32px" viewBox="0 -960 960 960" width="32px" fill="#e3e3e3">
                    <path d="M240-200h120v-200q0-17 11.5-28.5T400-440h160q17 0 28.5 11.5T600-400v200h120v-360L480-740 240-560v360Zm-80 0v-360q0-19 8.5-36t23.5-28l240-180q21-16 48-16t48 16l240 180q15 11 23.5 28t8.5 36v360q0 33-23.5 56.5T720-120H560q-17 0-28.5-11.5T520-160v-200h-80v200q0 17-11.5 28.5T400-120H240q-33 0-56.5-23.5T160-200Zm320-270Z"/>
                </svg>
                <span style="font-size: 32px; font-weight: 600; margin-left: 12px; color: #e3e3e3;">{translate("Home Page")}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center;">{translate("Welcome to the SBM Website!")}</p>', unsafe_allow_html=True)

        if st.button(translate("Login"), type="primary", key="home_page"):
            st.session_state.page = "login"
            st.rerun()
        if st.button(translate("Sign Up"), type="primary"):
            st.info(translate("Sign up is not implemented yet."))

    try:
        rain('•', 20, falling_speed=5, animation_length="infinite")
    except:
        pass

def login():
    r1col1, r1col2, r1col3 = st.columns([1, 0.5, 1])
    r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
    r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
    r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])

    with r1col2:
        st.title(translate("Login"))
    with r2col2:
        username = st.text_input(translate("Username"), placeholder=translate("Enter your username"))
    with r3col2:
        password = st.text_input(translate("Password"), placeholder=translate("Enter your password"), type="password")
    with r4col2:
        if st.button(translate("Login"), type="primary", key="login_page"):
            creds = {"username": username, "password": password}
            try:
                response = requests.post(f"{BASE_URL}/login", json=creds)
                if response.status_code == 200:
                    st.success(translate("Login successful!"))
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.password = password
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error(translate("Login failed. Please check your credentials."))
            except Exception as e:
                st.error(f"{translate('Request failed')}: {e}")

    rain('•', 20, falling_speed=5, animation_length="infinite")

class NavigationWidgets:
    def __init__(self):
        with st.sidebar:
            st.title("Navigation")
            if st.button(translate("Dashboard")):
                st.session_state.page = "dashboard"
                st.rerun()
            if st.button(translate("Settings")):
                st.session_state.page = "settings"
                st.rerun()
            if st.button(translate("Logout")):
                st.session_state.logged_in = False
                st.session_state.page = "home"
                st.session_state.username = ""
                st.session_state.password = ""
                st.rerun()

def dashboard():
    NavigationWidgets()
    st.title(f"{translate('Dashboard for')} {st.session_state.username}")
    st.write(translate("This is the dashboard page."))

def settings():
    NavigationWidgets()
    st.title(translate("Settings"))

    lang_code_map = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Hindi": "hi",
        "Chinese (Simplified)": "zh-cn",
    }

    inv_map = {v: k for k, v in lang_code_map.items()}
    current_lang = inv_map.get(st.session_state.language, "English")

    selected_lang = st.selectbox("🌐 Select Language", list(lang_code_map.keys()), index=list(lang_code_map.keys()).index(current_lang))
    st.session_state.language = lang_code_map[selected_lang]

    st.info(translate("Settings page content goes here."))

# --- Routing ---
page = st.session_state.page
if page == "home":
    homepage()
elif page == "login":
    login()
elif page == "dashboard":
    dashboard()
elif page == "settings":
    settings()
