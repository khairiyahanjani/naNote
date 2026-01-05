import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")

#option
def homepage():
    st.title("Homepage")
    if st.button("Catatan", "Kalkulasi Hasil PSA"):
        st.switch_page("page_1.py", query_params={"appy.py": "Homepage"})
        st.switch_page("page_2.py", query_params={"page_1.py": "Catatan"})

pg = st.navigation([homepage, "page_1.py"])
pg.run()
