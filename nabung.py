import streamlit as st

st.title("Ini halaman nabung")

with st.form("Nabung"):
    nama = st.text_input("Masukkan nama")
    nominal = st.number_input("Masukkan nominal nabung")
    submit_button = st.form_submit_button("Simpan")

    if submit_button:
        st.write(nama)
        st.session_state["Nabung"].append({
            "Nama" : nama,
            "Nominal" : nominal
        })

        st.success("Berhasil menabung!")