# 🎬 Movie Recommendation System

A sleek, content-based movie recommendation system built using Python and Streamlit. It analyzes movie metadata to suggest the most similar movies based on user preferences.

---

## 🚀 Live Demo

🔗 [Click here to view the live application](https://movie-recommendation-system-kv.streamlit.app/) *(Replace with your actual deployment link)*

---

## 📌 Overview

This project is designed to help users discover new movies by analyzing metadata such as **genres, keywords, cast, crew, and overviews**. By processing this textual data, the system calculates the similarity between different movies and recommends the top matches instantly.

---

## ⚙️ Tech Stack

*   **Language:** Python
*   **Data Libraries:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn
*   **Web Framework:** Streamlit
*   **Model Serialization:** Pickle

---

## 🧠 How It Works

1.  **Data Preprocessing:** Cleaning and combining movie datasets (handling missing values, parsing JSON structures for genres/cast).
2.  **Feature Extraction:** Creating a unified "tags" column combining genres, keywords, overview, cast, and director.
3.  **Vectorization:** Converting text tags into numerical vectors using `CountVectorizer` or `TF-IDF`.
4.  **Similarity Computation:** Applying **Cosine Similarity** to calculate the mathematical closeness between movie vectors.
5.  **Recommendation Engine:** Fetching the top 5 most similar movies based on the highest similarity scores.

---

## 📂 Project Structure

```text
├── dataset/                  # Raw TMDB movie datasets
├── app.py                    # Streamlit web application code
├── movie_recommender.ipynb   # Jupyter notebook for data analysis & model building
├── similarity.pkl            # Precomputed similarity matrix (generated)
├── movie_list.pkl            # Preprocessed movie dataframe (generated)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
