import streamlit as st

st.write("")

dashboard = st.Page("./Page/dashboard.py", title ="Dashboard")
nabung = st.Page("./Page/nabung.py", title ="Nabung")

pg = st.navigation({
    "Dashboard" : [dashboard],
    "Nabung" : [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state["Nabung"] = []

pg.run()