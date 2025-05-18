import streamlit as st
import datetime
from annotated_text import annotated_text
from streamlit_timeline import timeline
import json

# Page configuration
st.set_page_config(
    layout="wide",
    page_title="TEST CWS Subscription Viewer",
    initial_sidebar_state="expanded"
)



r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])
r4col1, r4col2, r4col3 = st.columns([0.25, 4, 0.25])



with r1col2:
    st.title("Login")
with r2col2:
    st.text_input("Username", placeholder="Enter your username")
with r3col2:
    st.text_input("Password", placeholder="Enter your password", type="password")
with r4col2:
    st.button("Login", type="primary")
    


