import os
import pickle

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


IMAGE_FOLDER = "images"
MOVIE_FILE = "Cleaned_Movies.csv"
SIMILARITY_FILE = "similarity.pkl"


st.set_page_config(page_title="Movie Recommender", layout="wide")


@st.cache_data
def load_movies():
    return pd.read_csv(MOVIE_FILE)


@st.cache_resource
def load_similarity(movies):
    if not os.path.exists(SIMILARITY_FILE):
        vectorizer = CountVectorizer(max_features=5000, stop_words="english")
        vectors = vectorizer.fit_transform(movies["tags"].fillna("")).toarray()
        return cosine_similarity(vectors)

    with open(SIMILARITY_FILE, "rb") as file:
        return pickle.load(file)


def image_path_for_title(title):
    for extension in (".jpg", ".jpeg", ".png"):
        path = os.path.join(IMAGE_FOLDER, f"{title}{extension}")
        if os.path.exists(path):
            return path
    return None


def recommend(selected_movies, movies, similarity):
    recommended_movies = []
    seen = set(selected_movies)

    for movie_name in selected_movies:
        if movie_name not in movies["title"].values:
            continue

        index = movies[movies["title"] == movie_name].index[0]
        similar_movies = sorted(
            list(enumerate(similarity[index])),
            key=lambda item: item[1],
            reverse=True,
        )[1:6]

        for movie_index, _score in similar_movies:
            title = movies.iloc[movie_index]["title"]
            if title not in seen:
                recommended_movies.append(title)
                seen.add(title)

    return recommended_movies


movies = load_movies()
similarity = load_similarity(movies)
movie_titles = sorted(movies["title"].dropna().unique())

st.title("Movie Recommender")

selected_movies = st.multiselect(
    "Select movies you like",
    movie_titles,
    placeholder="Choose one or more movies",
)

if st.button("Get Recommendations", type="primary"):
    if not selected_movies:
        st.warning("Please select at least one movie.")
    else:
        recommendations = recommend(selected_movies, movies, similarity)

        if recommendations:
            st.subheader("Recommended Movies")
            columns = st.columns(5)

            for index, movie in enumerate(recommendations):
                with columns[index % 5]:
                    poster = image_path_for_title(movie)
                    if poster:
                        st.image(poster, use_container_width=True)
                    st.caption(movie)
        else:
            st.info("No recommendations found for the selected movies.")
