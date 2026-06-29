# 🎬 Movie Recommender AI

An AI-powered movie recommendation system built with **Flask**, **Python**, and **Machine Learning** that suggests similar movies based on user-selected films through an interactive Netflix-inspired web interface.

![GitHub stars](https://img.shields.io/github/stars/Sourabhnamdev9981/movie-recommender-ai)
![GitHub forks](https://img.shields.io/github/forks/Sourabhnamdev9981/movie-recommender-ai)
![GitHub issues](https://img.shields.io/github/issues/Sourabhnamdev9981/movie-recommender-ai)

## ✨ Features

* 🎥 Browse movies with poster-based selection
* 🔍 Search movies instantly
* 🤖 AI-powered movie recommendations
* 🎨 Modern Netflix-inspired dark UI
* ➕ Add new movies and retrain recommendations
* ⚡ Fast content-based filtering using TF-IDF and Cosine Similarity

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* Scikit-learn
* HTML
* CSS
* JavaScript

## 📂 Project Structure

```text
Movie-Recommender-AI/
│
├── images/
├── templates/
├── recommender.py
├── Cleaned_Movies.csv
├── similarity.pkl
├── requirements.txt
├── Procfile
└── README.md

```

## 🧠 How It Works

1. User selects one or more movies.
2. Movie metadata is processed using TF-IDF vectorization.
3. Cosine similarity is calculated between movies.
4. The system recommends the most similar movies.

## 📸 Screenshots

### Homepage

![Homepage](screenshots/homepage.png)

### Search Feature

![Search](screenshots/search_movies.png)

### Recommendations

![Recommendations](screenshots/recommendations.png)

## 🔮 Future Improvements

* Movie posters for recommendation
* TMDB API integration
* User authentication
* Watchlist functionality
* Movie ratings and review
* Cloud deployment



