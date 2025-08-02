import streamlit as st

st.set_page_config(page_title="Book Genre Recommender", page_icon="📚")

st.title("📚 Book Genre Recommender")
st.subheader("Find your perfect book genre based on your interests")

# Questions
name = st.text_input("What's your name?")

interests = st.multiselect(
    "What themes or topics are you most drawn to?",
    ["Adventure", "Romance", "Mystery", "Science", "History", "Fantasy", "Horror", "Psychology", "Philosophy", "Comedy"]
)

fav_media = st.multiselect(
    "What kind of movies/TV shows do you enjoy?",
    ["Sci-Fi", "Historical", "Love Stories", "Detective", "Fantasy", "Horror", "Sitcoms", "Documentaries"]
)

length_pref = st.radio(
    "Preferred book length?",
    ["Short reads", "Medium", "Long novels"]
)

real_vs_imaginary = st.radio(
    "Which world do you prefer?",
    ["Real-world stories", "Imaginary worlds", "Both"]
)

mood = st.selectbox(
    "What mood are you usually in while reading?",
    ["Relaxing", "Excited", "Curious", "Romantic", "Spooked", "Inspired"]
)

if st.button("Suggest Genre"):
    st.write(f"Thanks, {name or 'reader'}! Here's your suggested genre(s):")

    suggestions = set()

    if "Romance" in interests or "Love Stories" in fav_media or mood == "Romantic":
        suggestions.add("Romance 💕")
    if "Mystery" in interests or "Detective" in fav_media or mood == "Curious":
        suggestions.add("Mystery / Thriller 🔍")
    if "Fantasy" in interests or "Fantasy" in fav_media or real_vs_imaginary == "Imaginary worlds":
        suggestions.add("Fantasy 🐉")
    if "Science" in interests or "Sci-Fi" in fav_media:
        suggestions.add("Science Fiction 🚀")
    if "History" in interests or "Historical" in fav_media:
        suggestions.add("Historical Fiction 🏛️")
    if "Horror" in interests or "Horror" in fav_media or mood == "Spooked":
        suggestions.add("Horror 👻")
    if "Comedy" in interests or "Sitcoms" in fav_media:
        suggestions.add("Humor / Satire 😂")
    if "Philosophy" in interests or mood == "Inspired":
        suggestions.add("Philosophical / Literary Fiction 📘")

    if not suggestions:
        suggestions.add("General Fiction 📚")

    for genre in suggestions:
        st.success(f"- {genre}")
