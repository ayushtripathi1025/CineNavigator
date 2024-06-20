# CineNavigator

Welcome to the CineNavigator repository, a content-based movie recommendation system designed to suggest movies based on attributes like genres, directors, actors, and plot summaries. Trained on a dataset of over 5000 movies, this system generates personalized recommendations for users.

## Libraries Used

- **Pandas**: Used for data manipulation and preprocessing.
- **NumPy**: Essential for numerical computations and data arrays.
- **scikit-learn**: Provides machine learning algorithms and utilities for model building and evaluation.
- **NLTK (Natural Language Toolkit)**: Used for text preprocessing and tokenization.
- **Streamlit**: Framework for building interactive web applications.

## Dataset

- **Source**: The movie dataset used in this project is sourced from the TMDB 5000 Movie Dataset.

## Process

1. The movie and credits datasets are merged and relevant columns selected.
2. Missing values are dropped, and data is cleaned and transformed to extract useful features.
3. Text data is preprocessed and combined into tags, which are vectorized using CountVectorizer.
4. Cosine similarity is computed for these vectors.
5. A recommendation function is implemented to suggest similar movies.
6. Finally, the processed data and similarity matrix are saved using pickle for future use.
