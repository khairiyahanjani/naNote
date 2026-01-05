import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

#option
def Kalkulasi():
    st.title("Kalkulasi Hasil PSA")
def Catatan():
    
pg = st.navigation(["page_1.py", Kalkulasi])
pg.run()
pg = st.navigation(["page_2.py", Catatan])
pg.run()
