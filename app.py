import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

#option
def Kalkulasi():
    st.title("Kalkulasi Hasil PSA")

pg = st.navigation(["page_1.py", Kalkulasi])
pg.run()

def Catatan():
    st.title("Mulai Catat")

pg = st.navigation(["page_2.py", Catatan])
pg.run()
