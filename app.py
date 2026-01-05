import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

def page_1():
    st.title("Catatan praktik")
    st.page_link("Kalkulasi Hasil PSA", query_params={"index.html": "Catatan praktik"})

pg = st.navigation([Catatan praktik, "Kalkulasi Hasil PSA"])
pg.run()

