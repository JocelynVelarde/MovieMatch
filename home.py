import streamlit as st

st.title('Get Started 📺')
st.divider()
st.write('Welcome to the home page')
st.write('This is a simple example of a Streamlit app')

st.divider()
st.page_link("pages/match.py", label="Click this button to start matching", icon="🚀")