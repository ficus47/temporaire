import streamlit as st

st.title("Exposée de Joseph")
st.balloons()

a = open("moi.docx", "rb").read()

st.download_button("telecharger l'explosée", data=a, file_name="explosée_de_joseph.docx", mime="plain/text")
