"""
prompts.py
-----------
Contains functions for building prompts for the Gemini API.
"""


def create_movie_prompt(
    genre,
    mood,
    language,
    actor,
    age_group,
    duration,
    number_of_movies,
):
    """
    Create a structured prompt for Gemini AI.

    Parameters
    ----------
    genre : str
    mood : str
    language : str
    actor : str
    age_group : str
    duration : str
    number_of_movies : int

    Returns
    -------
    str
        Prompt ready to send to Gemini.
    """

    prompt = f"""
You are an expert movie recommendation assistant.

Recommend exactly {number_of_movies} movies based on the following user preferences.

User Preferences:
-----------------
Genre: {genre}
Mood: {mood}
Preferred Language: {language}
Favorite Actor: {actor}
Age Group: {age_group}
Preferred Movie Duration: {duration}

Instructions:

1. Recommend only high-quality movies.
2. Avoid duplicate recommendations.
3. Prefer movies matching the selected language.
4. If the favorite actor appears in suitable movies, prioritize those.
5. Ensure recommendations are appropriate for the selected age group.
6. Recommend movies that fit the user's mood.
7. Include a mix of popular and highly rated films whenever possible.

For each movie provide:

🎬 Movie Title

📅 Release Year

⭐ IMDb Rating

🎭 Genre

⏱ Approximate Duration

📝 Short Story (2-3 lines)

❤️ Why this movie matches the user's preferences

Format the response using Markdown with clear headings and bullet points.

End the response with a short sentence encouraging the user to enjoy the movies.
"""

    return prompt