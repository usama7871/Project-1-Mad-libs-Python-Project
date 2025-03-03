import streamlit as st
from story_templates import get_story_templates
import random

# Set up the app title and description
st.set_page_config(page_title="Mad Libs Game", layout="wide")
st.title("Mad Libs Game")
st.write("Fill in the blanks to generate your funny story!")

# User management
st.sidebar.header("User Management")
username = st.sidebar.text_input("Enter your username:")
password = st.sidebar.text_input("Enter your password:", type="password")

# In-memory user storage
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# User registration
if st.sidebar.button("Register"):
    if username and password:
        st.session_state.users[username] = {'password': password, 'saved_stories': []}
        st.sidebar.success("User registered successfully!")
    else:
        st.sidebar.error("Please enter a username and password.")

# User login
if st.sidebar.button("Login"):
    if username in st.session_state.users and st.session_state.users[username]['password'] == password:
        st.session_state.current_user = username
        st.sidebar.success("Logged in successfully!")
    else:
        st.sidebar.error("Invalid username or password.")

# Collect user inputs
st.header("Story Inputs")
noun_options = ["cat", "dog", "car", "house"]
verb_options = ["run", "jump", "swim", "dance"]
adjective_options = ["happy", "sad", "funny", "silly"]
adverb_options = ["quickly", "silently", "happily", "sadly"]

noun = st.selectbox("Choose a noun:", noun_options)
verb = st.selectbox("Choose a verb:", verb_options)
adjective = st.selectbox("Choose an adjective:", adjective_options)
adverb = st.selectbox("Choose an adverb:", adverb_options)
place = st.text_input("Enter a place:")
animal = st.text_input("Enter an animal:")
story_templates = get_story_templates()
story_template = st.selectbox("Choose a story template:", list(story_templates.keys()), index=0)

# Generate and display the story when the button is clicked
if st.button("Generate Story") and st.session_state.current_user:  # Ensure user is authenticated
    magical_elements = ["a dragon", "a unicorn", "a wizard", "a fairy"]
    random_element = random.choice(magical_elements)
    story = story_templates[story_template].format(
        adjective=adjective,
        noun=noun,
        verb=verb,
        adverb=adverb,
        place=place,
        magical_element=random_element
    )
    st.subheader("Your Magical Mad Libs Story")
    st.write(story)

    # Save the generated story for the user
    st.session_state.users[st.session_state.current_user]['saved_stories'].append(story)

# Display saved stories
if st.button("View Saved Stories") and st.session_state.current_user:
    st.subheader("Your Saved Stories")
    saved_stories = st.session_state.users[st.session_state.current_user]['saved_stories']
    if saved_stories:
        for saved_story in saved_stories:
            st.write(saved_story)
    else:
        st.write("No saved stories yet.")

# Settings management
st.sidebar.header("Settings")
if st.sidebar.button("Change Theme"):
    new_theme = st.sidebar.selectbox("Select Theme:", ["light", "dark"])
    st.session_state.theme = new_theme
    st.sidebar.success(f"Theme changed to {new_theme}.")
    
# Apply the selected theme
if 'theme' in st.session_state:
    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
            .reportview-container {
                background-color: #2E2E2E;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
