import streamlit as st
import datetime
from annotated_text import annotated_text
from streamlit_timeline import timeline
import json
from streamlit_extras.let_it_rain import rain

# Page configuration
st.set_page_config(
    page_title="2 TEST CWS Subscription Viewer",
)



r1col1, r1col2, r1col3 = st.columns([1, 0.5, 1])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])



with r1col2:
    st.title("Login")
with r2col2:
    st.session_state.username = st.text_input("Username", placeholder="Enter your username")
with r3col2:
    st.session_state.password = st.text_input("Password", placeholder="Enter your password", type="password")
with r4col2:
    st.button("Login", type="primary")
    

# Trigger the rain
rain('•', 20, falling_speed=5, animation_length="infinite")