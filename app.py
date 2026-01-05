import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

#option
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("Catatan Praktik", "page_1.py")
st.page_link("Kalkulasi Hasil PSA", "page_2.py")
