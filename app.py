import streamlit as st
from PIL import Image

from utils.prompts import create_movie_prompt
from utils.gemini import generate_movie_recommendations


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# LOAD BANNER IMAGE
# ---------------------------------------------------------

try:
    banner = Image.open("assets/movie_banner.jpg")
except FileNotFoundError:
    banner = None


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 45px;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
    }

    .sub-title {
        color: #CCCCCC;
        font-size: 18px;
        text-align: center;
    }

    .stButton > button {
        width: 100%;
        background-color: #E50914;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #B20710;
        color: white;
    }

    .movie-card {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #E50914;
    }

    .block-container {
        padding-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# DISPLAY BANNER
# ---------------------------------------------------------

if banner:
    st.image(
        banner,
        use_container_width=True
    )


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.title("🎬 AI Movie Recommender")

    st.divider()

    st.header("📖 About")

    st.info(
        """
This application recommends movies
using **Google Gemini AI**.

The app analyzes your preferences
and generates personalized movie
recommendations using Gemini API.

Your API key is securely stored
inside the `.env` file.
"""
    )

    st.divider()

    st.header("🎭 Genres")

    st.markdown(
        """
        - Action
        - Comedy
        - Horror
        - Drama
        - Sci-Fi
        - Romance
        - Thriller
        - Fantasy
        """
    )

    st.divider()

    st.header("😊 Available Moods")

    st.markdown(
        """
        - Happy
        - Sad
        - Excited
        - Relaxed
        - Romantic
        - Motivational
        - Scary
        """
    )

    st.divider()

    st.success(
        "Built with ❤️ Streamlit + Gemini AI"
    )


# ---------------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------------

st.markdown(
    """
    <h1 class="main-title">
    🎬 AI Movie Recommender
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <p class="sub-title">
    Discover your next favorite movie using Artificial Intelligence.
    </p>
    """,
    unsafe_allow_html=True
)


st.divider()


# ---------------------------------------------------------
# USER INPUT SECTION
# ---------------------------------------------------------

left, right = st.columns(2)


with left:

    genre = st.selectbox(
        "🎭 Select Movie Genre",
        [
            "Action",
            "Comedy",
            "Drama",
            "Romance",
            "Sci-Fi",
            "Fantasy",
            "Thriller",
            "Horror"
        ]
    )


    language = st.selectbox(
        "🌍 Preferred Language",
        [
            "English",
            "Hindi",
            "Telugu",
            "Tamil",
            "Malayalam",
            "Korean",
            "Japanese"
        ]
    )


    actor = st.text_input(
        "🎥 Favorite Actor",
        placeholder="Example: Tom Cruise"
    )



with right:

    mood = st.radio(
        "😊 Current Mood",
        [
            "Happy",
            "Sad",
            "Excited",
            "Relaxed",
            "Romantic",
            "Motivational",
            "Scary"
        ]
    )


    age_group = st.selectbox(
        "👨‍👩‍👧 Age Group",
        [
            "Kids",
            "Teen",
            "Adult",
            "Family"
        ]
    )


    duration = st.selectbox(
        "⏱ Movie Duration",
        [
            "Under 2 Hours",
            "2-3 Hours",
            "No Preference"
        ]
    )


    movie_count = st.slider(
        "🎞 Number of Recommendations",
        min_value=3,
        max_value=10,
        value=5
    )


st.divider()


# ---------------------------------------------------------
# GENERATE MOVIE RECOMMENDATIONS
# ---------------------------------------------------------

generate = st.button(
    "🎬 Recommend Movies",
    use_container_width=True
)


st.subheader(
    "🍿 AI Movie Recommendations"
)


if generate:

    if actor.strip() == "":

        st.error(
            "⚠ Please enter your favorite actor."
        )


    else:

        try:

            # Create Gemini Prompt

            prompt = create_movie_prompt(
                genre=genre,
                mood=mood,
                language=language,
                actor=actor,
                age_group=age_group,
                duration=duration,
                number_of_movies=movie_count
            )


            # Gemini API Call

            with st.spinner(
                "🎬 Gemini AI is finding movies for you..."
            ):

                response = generate_movie_recommendations(prompt)


            st.success(
                "✅ Recommendations Generated Successfully!"
            )


            st.divider()


            st.markdown(
                response
            )


        except Exception:

            st.error(
                """
                ❌ Unable to generate recommendations.

                Please check:
                - Gemini API key
                - Internet connection
                - API configuration
                """
            )