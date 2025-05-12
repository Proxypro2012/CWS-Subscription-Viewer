r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([0.25, 4, 0.25])
r3col1, r3col2, r3col3 = st.columns([0.25, 4, 0.25])



with r1col2:
  st.title("Date Picker Test")
with r2col2:
  st.divider()
with r3col2:
  selected_date = st.date_input("Pick a date", datetime.date.today())
  st.write("You selected:", selected_date)

