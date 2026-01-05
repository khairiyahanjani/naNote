import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")
color = st.get_option("theme.primaryColor")

#option
if st.button("Catatan"):
    st.switch_page("pages/page_1.py")
if st.button("Kalkulasi"):
    st.switch_page("pages/page_2.py")
