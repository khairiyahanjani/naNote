import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

#option
st.page_link_button("Catatan Praktik", "page_1.py")
pg = st.navigation([page_1, "page_2.py"])
pg.run()

st.page_link_button("Kalkulasi Hasil PSA", "page_2.py")
pg = st.navigation([page_2, "page_1.py"])
pg.run()
