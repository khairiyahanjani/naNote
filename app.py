import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik")

st.button("Mulai pencatatan", type="primary")
if st.button("Catat"):
    st.int(input(" "))
else :
    st.write("tercatat")
