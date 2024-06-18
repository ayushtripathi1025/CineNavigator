import streamlit as st
import pickle
import requests


# Function to fetch poster URL using movie ID from TMDB API
def fetch_poster(movie_id):
    # Make API request to fetch movie details
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8af6b27aa15228c09a9a7dfe8c790aab&language=en-US'.format(
            movie_id))
    fetch_data = response.json()
    # Construct poster URL
    return "https://image.tmdb.org/t/p/original/" + fetch_data['poster_path']


# Function to recommend movies based on input movie
def recommend_fn(movie):
    # Get index of selected movie in dataframe
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    # Retrieve similarity scores for selected movie
    distances = similarity[movie_index]
    # Sort movies based on similarity scores and select top 5 recommended movies
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []
    # Iterate through recommended movies and fetch their posters
    for i in movies:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommend_movies.append(movies_df.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_poster


# Load preprocessed movie data and similarity matrix from pickle files
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown to select a movie for recommendations
selected_movie = st.selectbox(
    'Select your movie to get recommendations!',
    movies_list
)

# Button to trigger recommendations
if st.button('Recommend'):
    # Get recommended movies and their posters
    names, posters = recommend_fn(selected_movie)

    # Display recommended movies and their posters in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
