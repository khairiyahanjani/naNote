import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")
color = st.get_option("theme.primaryColor")

#option
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Catatan", icon="1️⃣")
st.page_link("pages/page_2.py", label="Kalkulasi Hasil PSA", icon="2️⃣")
st.page_link("http://www.google.com", label="Google", icon="🌎")
