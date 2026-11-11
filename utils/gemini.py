"""
gemini.py
-----------------------
Handles Gemini API configuration and communication.
"""

import os

import google.generativeai as genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Read Gemini API Key from .env
API_KEY = os.getenv("GEMINI_API_KEY")


def configure_gemini():
    """
    Configure the Gemini API.

    Returns
    -------
    GenerativeModel
        Configured Gemini model.
    """

    if not API_KEY:
        raise ValueError(
            "Gemini API Key not found. Please add GEMINI_API_KEY to your .env file."
        )

    # Configure Gemini
    genai.configure(api_key=API_KEY)

    # Create Gemini Model
    model = genai.GenerativeModel("gemini-3.5-flash")

    return model


def generate_movie_recommendations(prompt):
    """
    Sends the prompt to Gemini and returns the AI response.

    Parameters
    ----------
    prompt : str
        Prompt generated in prompts.py

    Returns
    -------
    str
        AI generated movie recommendations.
    """

    try:

        model = configure_gemini()

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "No response was generated."

    except Exception as error:
        raise RuntimeError(f"Gemini API Error: {error}")