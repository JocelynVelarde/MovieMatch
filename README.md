
# Movie Matcher with Sentiment Analysis 🚀

We decided to explore the recommendation of movies with a K cluster ML system by taking the tags of movies such as ratings, directors, and actors and determining the audiences that coincide with the systems. This is done with a database from tmbd that contains data from around 5,000 movies.

<img src="https://github.com/JocelynVelarde/MovieMatch/assets/70779495/d5da2595-d429-41ef-8bdc-77838e1a26e5" alt="safenav profile" width="500" height="400">

## Authors

- [@JocelynVelarde](https://github.com/JocelynVelarde)
- [@Diego785xd](https://github.com/Diego785xd)


## Features

- Select 3 movies from our database
- Movie recommendation using ML Algorithm kmeans
- Implements LLMs to filter requests and provide feedback data
- Light and Dark mode enabled
- Available in all devices


## Structure
```bash
streamlit_app 
├─ home.py
├─ .streamlit
│   └─ secrets.toml
│   └─ gcloud.json
├─ algorithms
|  └─ movie_model.pkl
|  └─ moviesPredictor.py
├─ api
├─ assets
│  └─ files
│  └─ images
├─ pages
│  └─ report_bug.py
│  └─ match.py
└─ requirements.txt
```

## Tools

- OpenAI API
- Streamlit
- Google Sheets API
- scipy

Deployed with: Streamlit Cloud

## Demo

[YouTube](https://www.youtube.com/watch?v=M9DtZs3MAUk&t=4s)


## License

[MIT](https://choosealicense.com/licenses/mit/)



