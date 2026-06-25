# 🎬 Movie Recommendation System

A sleek, content-based movie recommendation system built using Python and Streamlit. It analyzes movie metadata to suggest the most similar movies based on user preferences.

---

## 🚀 Live Demo

🔗 [Click here to view the live application](https://movie-recommendation-system-kv.streamlit.app/)

---

## 📌 Overview

This project is designed to help users discover new movies by analyzing metadata such as **genres, keywords, cast, crew, and overviews**. By processing this textual data, the system calculates the similarity between different movies and recommends the top matches instantly.

---

## ⚙️ Tech Stack

*   **Language:** Python
*   **Data Libraries:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn (CountVectorizer, Cosine Similarity)
*   **Web Framework:** Streamlit
*   **Model Serialization:** Pickle

---

## 🧠 Core Theory & Architecture

This system relies on **Content-Based Filtering**, meaning it recommends items similar to what a user likes, based on the item attributes (metadata) rather than user behavior.

### 1. Data Preprocessing & Feature Engineering
*   **Data Merging:** Combining movie datasets (metadata and credits) using unique identifiers.
*   **Cleaning:** Extracting names from complex JSON/stringified columns (like extracting top 3 actors from `cast` or the director from `crew`).
*   **Tag Generation:** Merging all textual descriptive elements—`overview`, `genres`, `keywords`, `cast`, and `director`—into a single large string block called **"tags"** for each movie.

### 2. Text Vectorization (The Mathematical Representation)
Computers don't understand raw text, so we convert the "tags" into numerical vectors. 
*   **Bag of Words (CountVectorizer):** We tokenized the tags and extracted the top $N$ (e.g., 5,000) most frequent words across all movies, excluding common English stop words (*and, the, is, etc.*).
*   Each movie is then represented as a vector in an $N$-dimensional space, where the value at each coordinate represents the frequency of a specific word in that movie's tags.

### 3. Measuring Proximity (Cosine Similarity)
Instead of calculating the Euclidean distance (which can be biased by the length of the text/tags), we calculate the **Cosine Similarity** between the movie vectors.

Mathematically, it measures the cosine of the angle between two multi-dimensional vectors:
$$\text{Similarity}(A, B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$$

*   A value close to **1** means the angle is $0^\circ$, implying the movies are highly similar.
*   A value close to **0** implies no textual or contextual overlap.

---

## 📂 Project Structure

```text
├── data/                     # Raw or preprocessed TMDB datasets
├── models/                   # Serialized pickle files (.pkl) for the app
├── app.py                    # Streamlit web application frontend/backend
├── .gitignore                # Specifies intentionally untracked files to ignore
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
