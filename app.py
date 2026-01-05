import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

def page_1():
    st.title("Catatan praktik")
    st.page_link("page_2", query_params={"page_1": "Catatan praktik"})
pg = st.navigation([page_1, "page_2"])
pg.run()

def page_2():
    st.title("Kalkulasi Hasil PSA")
    st.page_link("page_1", query_params={"page_2": "Kalkulasi Hasil PSA"})
pg = st.navigation([page_2, "page_1"])
pg.run()

