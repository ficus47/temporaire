import streamlit as st

st.title("Exposée de Joseph")
st.balloons()

a = open("Joseph.txt", "rb").read()

st.download_button("telecharger l'explosée", data=a, file_name="Joseph.txt", mime="text/plain")

st.write("je m'excuse pour la mise en forme mais mon hebergeur ne supporte pas les fichier autre que png et txt")
