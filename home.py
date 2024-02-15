import streamlit as st

st.title('Get Started 📺')
st.divider()
st.write('We decided to explore the recommendation of movies with a K cluster ML system by taking the tags of movies such as ratings, directors, and actors and determining the audiences that coincide with the systems. This is done with a database from tmbd that contains data from around 5,000 movies.')

st.write('Follow this steps to get started:')
st.write('1. Click the button below to start the matching process')
st.write('2. Enter the name of the movie you want to compare')
st.write('3. Click the button to get the recommendations')
st.write('4. Enjoy the recommendations')

st.divider()
st.write("Additionally, you can also type in how you felt with the recommendations, and we will take that information in consideration for future instances.")

st.divider()
st.page_link("pages/match.py", label="Click this button to start matching", icon="🚀")