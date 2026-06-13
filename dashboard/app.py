import streamlit as st
import sys
import os

# Add project root to Python path
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from recommender.content_based import recommend, movies
from recommender.bollywood_recommender import recommend_bollywood

st.set_page_config(
    page_title="Global CineMind AI",
    page_icon="🎬",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎬 Global CineMind AI")

st.sidebar.info(
    """
    AI-Powered Movie Recommendation System

    Features:
    ✔ Hollywood Recommendations
    ✔ Bollywood Recommendations
    ✔ Content-Based Filtering
    ✔ Streamlit Dashboard
    """
)

# Main Title
st.title("🎬 Global CineMind AI")
st.subheader(
    "Hollywood + Bollywood Movie Recommendation System"
)

# Statistics
st.metric(
    "Movies Available",
    len(movies)
)

# Industry Selection
industry = st.selectbox(
    "Choose Industry",
    ["Hollywood", "Bollywood"]
)

# Movie Input
movie_name = st.text_input(
    "Enter Movie Name"
)

# Recommendation Button
if st.button("Recommend"):

    if not movie_name:
        st.warning(
            "Please enter a movie name."
        )
        st.stop()

    try:

        if industry == "Hollywood":

            matches = movies[
                movies["title"].str.contains(
                    movie_name,
                    case=False,
                    na=False
                )
            ]

            if len(matches) == 0:
                st.error(
                    "Hollywood movie not found!"
                )
                st.stop()

            selected_movie = matches.iloc[0]["title"]

            recommendations = recommend(
                selected_movie
            )

        else:

            selected_movie = movie_name

            recommendations = recommend_bollywood(
                selected_movie
            )

        st.success(
            f"Selected: {selected_movie}"
        )

        st.markdown("## 🎬 Recommended Movies")

        for movie in recommendations[:10]:

            st.markdown(
                f"""
                <div style="
                    padding:15px;
                    border-radius:10px;
                    background-color:#f0f2f6;
                    margin-bottom:10px;
                    font-size:18px;
                ">
                    ⭐ <b>{movie}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using Python, Pandas, Scikit-Learn and Streamlit"
)