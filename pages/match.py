import streamlit as st
import pandas as pd
from streamlit_searchbox import st_searchbox

st.title('Movie Selection 🎬')
st.divider()
st.write('Select 3 movies to get recommendations')

df = pd.read_csv('assets/files/movies.csv')

movies = df['title'].tolist()

selected_movies = st.multiselect(
    label="Select Movies",
    options=movies,
    default=movies[:3],  
)

if len(selected_movies) > 3:
    st.warning('You can only select 3 movies.')
    selected_movies = selected_movies[:3]

if st.button('Get Recommendations'):
    st.success('Recommendations are ready!')



st.divider()

st.page_link("pages/report a bug.py", label="Click this button to Report a bug", icon="🐞")
