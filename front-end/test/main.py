import streamlit as st
import datetime
from annotated_text import annotated_text
from streamlit_timeline import timeline

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
menuOptions = ["Date Picker Test", "Modal Dailog (Popup)", "Annotated Text", "Timeline"]
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

if selected_page == menuOptions[0]:
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
if selected_page == menuOptions[1]:
    
    @st.dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()
    
    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"

if selected_page == menuOptions[2]:
  
  annotated_text(
      "This ",
      ("is", "verb"),
      " some ",
      ("annotated", "adj"),
      ("text", "noun"),
      " for those of ",
      ("you", "pronoun"),
      " who ",
      ("like", "verb"),
      " this sort of ",
      ("thing", "noun"),
      "."
  )
    
elif selected_page == menuOptions[3]:
    with open('example.json', "r") as f:
      data = f.read()

  # render timeline
    timeline(data, height=800)