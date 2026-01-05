import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")
st.imagebackground("dinokuning.jpg")

#Information tentang apk
expander = st.expander("🐡Apa itu naNote?")
expander.write('''
    naNote merupakan aplikasi berbasis web yang dirancang oleh mahasiswa/i Politeknik AKA Bogor
    untuk membantu praktikkan mencatat saat praktik dan membantu praktikkan mengkalkulasi
    hasil data PSA yang di dapat.
''')
expander.image("https://www.microtrac.com/images/5545e7b51b645ef7b0b93088a878cd6c/1200x/max/alpha/pic-wave-ii.jpg")

#option
if st.button("Catatan"):
    st.switch_page("pages/catatan_1.py", query_params={"page": "catatan"})
if st.button("Kalkulasi"):
    st.switch_page("pages/kalkulasi_2.py", query_params={"page": "kalkulasi"})
