import streamlit as st

# Page setup
st.set_page_config(page_title="Book Genre Recommender", page_icon="📚")

st.title("📚 Book Genre Recommender")
st.subheader("Discover your ideal book genres — and get some great titles to start with!")

# Questionnaire
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

# Genre-to-book mapping
book_recommendations = {
    "Romance 💕": [
        "Pride and Prejudice by Jane Austen",
        "The Notebook by Nicholas Sparks",
        "It Ends With Us by Colleen Hoover"
    ],
    "Mystery / Thriller 🔍": [
        "Gone Girl by Gillian Flynn",
        "The Girl with the Dragon Tattoo by Stieg Larsson",
        "The Da Vinci Code by Dan Brown"
    ],
    "Fantasy 🐉": [
        "Harry Potter Series by J.K. Rowling",
        "The Name of the Wind by Patrick Rothfuss",
        "A Court of Thorns and Roses by Sarah J. Maas"
    ],
    "Science Fiction 🚀": [
        "Dune by Frank Herbert",
        "The Martian by Andy Weir",
        "Neuromancer by William Gibson"
    ],
    "Historical Fiction 🏛️": [
        "The Book Thief by Markus Zusak",
        "All the Light We Cannot See by Anthony Doerr",
        "The Nightingale by Kristin Hannah"
    ],
    "Horror 👻": [
        "The Shining by Stephen King",
        "The Haunting of Hill House by Shirley Jackson",
        "Mexican Gothic by Silvia Moreno-Garcia"
    ],
    "Humor / Satire 😂": [
        "Good Omens by Neil Gaiman & Terry Pratchett",
        "Catch-22 by Joseph Heller",
        "Me Talk Pretty One Day by David Sedaris"
    ],
    "Philosophical / Literary Fiction 📘": [
        "Siddhartha by Hermann Hesse",
        "The Stranger by Albert Camus",
        "Norwegian Wood by Haruki Murakami"
    ],
    "General Fiction 📚": [
        "Where the Crawdads Sing by Delia Owens",
        "Eleanor Oliphant Is Completely Fine by Gail Honeyman",
        "Little Fires Everywhere by Celeste Ng"
    ]
}

# Logic to generate genre suggestions
if st.button("Suggest Genre and Books"):
    st.write(f"Thanks, {name or 'reader'}! Based on your answers:")

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
        st.markdown(f"### 🎯 {genre}")
        st.write("Recommended books:")
        for book in book_recommendations.get(genre, []):
            st.write(f"- {book}")

