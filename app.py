import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

def page_1():
    st.title("Catatan praktik")
    st.page_link("kalkulasi.html", query_params={"index.html": "Catatan praktik"})
pg = st.navigation([page_1, "kalkulasi.html"])
pg.run()

def page_2():
    st.title("Kalkulasi Hasil PSA")
    st.page_link("index.html", query_params={"kalkulasi.html": "Kalkulasi Hasil PSA"})
pg = st.navigation([page_2, "index.html"])
pg.run()

