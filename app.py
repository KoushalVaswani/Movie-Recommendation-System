import streamlit as st
import pickle

movies = pickle.load(open('models/movies.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

div[data-testid="stMetric"]{
    background-color:#1e293b;
    padding:15px;
    border-radius:12px;
}

.stProgress > div > div > div > div {
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stButton > button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

div[data-testid="stMetric"]{
    background-color:#1e293b;
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommendation System")

st.markdown(
    "Get personalized movie recommendations instantly!"
)
selected_movie = st.selectbox(
    "Search Movie",
    movies['title'].values
)

num_recommendations = st.number_input(
    "Number of Recommendations",
    min_value=1,
    max_value=20,
    value=5,
    step=1
)

col1, col2, col3 = st.columns(3)

col1.metric("Movies", len(movies))
col2.metric("Recommendations", num_recommendations)
col3.metric("Algorithm", "Content-Based")

st.sidebar.info("""
### 👨‍💻 Developer

**Koushal Vaswani**

🚀 Machine Learning Student

🧠 Content-Based Filtering

📊 Count Vectorizer

📐 Cosine Similarity

""")

st.sidebar.link_button(
    "🟦 LinkedIn",
    "https://www.linkedin.com/in/koushal-vaswani-56dg65/"
)

st.sidebar.link_button(
    "🐙 GitHub",
    "https://github.com/KoushalVaswani"
)


st.markdown("""
<style>
.big-font {
    font-size:40px !important;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

def recommend(movie , num_recommendations):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:num_recommendations+1]

    recommended_movies = []
    scores = []
    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )
        max_score = movies_list[0][1]

        scores.append(
        round((i[1] / max_score) * 100, 2)
        )

    return recommended_movies,scores


import time
if st.button("🎬 Get Recommendations"):

    with st.spinner("Finding similar movies... 🎬"):
        time.sleep(3)
    recommendations, scores = recommend(selected_movie , num_recommendations)
    st.subheader("🎬 Recommended Movies")
    st.success(
                f"Showing top {num_recommendations} recommendations for '{selected_movie}'"
            )
    cols = st.columns(min(num_recommendations, 5))

    for i in range(len(recommendations)):

        with st.container(border=True):

            st.markdown(f"### 🎬 {recommendations[i]}")

            st.write(
                f"🎯 Match Score: {scores[i]}%"
            )

            st.progress(scores[i]/100) 
               

