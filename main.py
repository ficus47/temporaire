import streamlit as st

st.title("Exposée de Joseph")
st.balloon(num_balloons=50)

a = open("moi.docx", "rb").read()

st.download_button("telecharger l'explosée", data=a, file_name="explosée_de_joseph.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
