import streamlit as st
import datetime

# Page configuration
st.set_page_config(
    layout="wide",
    page_title="TEST CWS Subscription Viewer",
    initial_sidebar_state="expanded"
)

r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])



# Sidebar
menuOptions = ["Date Picker Test", "Modal Dailog (Popup)"]
selected_page = st.sidebar.radio("", options=menuOptions)

months = {
  "1" : "January",
  "2" : "Febuary",
  "3" : "March",
  "4" : "April",
  "5" : "May",
  "6" : "June",
  "7" : "July",
  "8" : "August",
  "9" : "September",
  "10" : "October",
  "11" : "November",
  "12" : "December",
}

with r1col2:
  st.title("Date Picker Test")
with r2col2:
  st.divider()
with r3col2:
  selected_date = st.date_input("Pick a date", datetime.date.today())
  st.write("You selected:", selected_date)

  # ASSIGNING VALUES
  month = selected_date.month   #str(selected_date).strip('-')[1]
  year =  selected_date.year   #str(selected_date).strip('-')[0]

  st.write(year)
  st.write(month)

