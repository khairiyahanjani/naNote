import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")
color = st.get_option("theme.primaryColor")

#option
if st.button("Catatan"):
    st.switch_page("page_1.py", query_params={"page_1.py": "Catatan"})
if st.button("Kalkulasi"):
    st.switch_page("page_2.py", query_params={"page_2.py": "Kalkulasi"})
