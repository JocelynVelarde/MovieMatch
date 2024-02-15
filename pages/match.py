import streamlit as st
import pandas as pd
from api.gsheet_auth import gsheet_auth
from api.sentiment_gpt import ask_gpt

client = gsheet_auth()
sheet = client.open('MovieMatch Streamlit').worksheet('Hoja 1')

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
    row = [[selected_movies[0], selected_movies[1], selected_movies[2]]]
    sheet.insert_cols(row, 1)
    st.success('Recommendations are ready!')

container = st.container(border=True)
container.text("The movies display here")

st.divider()

st.subheader("Tell us how you felt watching the movies 💖")
prompt = st.text_area("We will take this feedback in consideration for future recommendations:")

if st.button("Submit to get feedback about your sentiment"):
    response = ask_gpt(prompt)
    st.write(response)

st.page_link("pages/report a bug.py", label="Click this button to Report a bug", icon="🐞")
