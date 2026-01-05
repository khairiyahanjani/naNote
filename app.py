import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

def page_1():
    st.title("Catatan praktik")
    st.page_link("page_2.py", query_params={"page_1.py": "Catatan praktik"})
pg = st.navigation([page_1, "page_2.py"])
pg.run()


