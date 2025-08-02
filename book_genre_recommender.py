import streamlit as st

# Page setup
st.set_page_config(page_title="Book Genre Recommender", page_icon="📚")

st.title("📚 Book Genre Recommender")
st.subheader("Get personalized book genres and titles based on your age and interests!")

# Questionnaire
name = st.text_input("What's your name?")
age = st.number_input("How old are you?", min_value=5, max_value=100, value=18)

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

# Genre → Age → Book list
genre_book_map = {
    "Romance 💕": {
        "child": ["Love You Forever by Robert Munsch"],
        "teen": ["To All the Boys I've Loved Before by Jenny Han", "Everything, Everything by Nicola Yoon"],
        "adult": ["The Notebook by Nicholas Sparks", "It Ends With Us by Colleen Hoover", "The Rosie Project by Graeme Simsion"]
    },
    "Mystery / Thriller 🔍": {
        "child": ["The Boxcar Children by Gertrude Chandler Warner", "Encyclopedia Brown by Donald J. Sobol"],
        "teen": ["One of Us Is Lying by Karen M. McManus", "A Good Girl's Guide to Murder by Holly Jackson"],
        "adult": ["Gone Girl by Gillian Flynn", "The Girl with the Dragon Tattoo by Stieg Larsson", "The Silent Patient by Alex Michaelides"]
    },
    "Fantasy 🐉": {
        "child": ["Harry Potter and the Sorcerer's Stone by J.K. Rowling", "The Lion, the Witch and the Wardrobe by C.S. Lewis"],
        "teen": ["Percy Jackson by Rick Riordan", "Throne of Glass by Sarah J. Maas"],
        "adult": ["The Name of the Wind by Patrick Rothfuss", "A Court of Thorns and Roses by Sarah J. Maas", "Mistborn by Brandon Sanderson"]
    },
    "Science Fiction 🚀": {
        "child": ["A Wrinkle in Time by Madeleine L’Engle", "The Wild Robot by Peter Brown"],
        "teen": ["Cinder by Marissa Meyer", "Skyward by Brandon Sanderson"],
        "adult": ["Dune by Frank Herbert", "The Martian by Andy Weir", "Project Hail Mary by Andy Weir"]
    },
    "Historical Fiction 🏛️": {
        "child": ["Number the Stars by Lois Lowry", "Sarah, Plain and Tall by Patricia MacLachlan"],
        "teen": ["Between Shades of Gray by Ruta Sepetys", "Salt to the Sea by Ruta Sepetys"],
        "adult": ["The Book Thief by Markus Zusak", "All the Light We Cannot See by Anthony Doerr", "The Nightingale by Kristin Hannah"]
    },
    "Horror 👻": {
        "child": ["Coraline by Neil Gaiman", "Goosebumps by R.L. Stine"],
        "teen": ["There's Someone Inside Your House by Stephanie Perkins", "Anna Dressed in Blood by Kendare Blake"],
        "adult": ["The Shining by Stephen King", "Mexican Gothic by Silvia Moreno-Garcia", "Bird Box by Josh Malerman"]
    },
    "Humor / Satire 😂": {
        "child": ["Diary of a Wimpy Kid by Jeff Kinney", "Captain Underpants by Dav Pilkey"],
        "teen": ["The Absolutely True Diary of a Part-Time Indian by Sherman Alexie", "Fangirl by Rainbow Rowell"],
        "adult": ["Good Omens by Neil Gaiman & Terry Pratchett", "Catch-22 by Joseph Heller", "Me Talk Pretty One Day by David Sedaris"]
    },
    "Philosophical / Literary Fiction 📘": {
        "child": ["The Little Prince by Antoine de Saint-Exupéry"],
        "teen": ["Tuesdays with Morrie by Mitch Albom", "The Alchemist by Paulo Coelho"],
        "adult": ["Siddhartha by Hermann Hesse", "The Stranger by Albert Camus", "Norwegian Wood by Haruki Murakami"]
    },
    "General Fiction 📚": {
        "child": ["Charlotte's Web by E.B. White", "Holes by Louis Sachar"],
        "teen": ["Wonder by R.J. Palacio", "Speak by Laurie Halse Anderson"],
        "adult": ["Where the Crawdads Sing by Delia Owens", "Little Fires Everywhere by Celeste Ng", "The Midnight Library by Matt Haig"]
    }
}

# Get age group
def get_age_group(age):
    if age <= 12:
        return "child"
    elif age <= 17:
        return "teen"
    else:
        return "adult"

# Get up to 5 books for a genre based on age group
def get_books_for_genre(genre, age_group, count=5):
    age_priority = [age_group] + [g for g in ['child', 'teen', 'adult'] if g != age_group]
    seen = set()
    books = []

    for group in age_priority:
        for book in genre_book_map.get(genre, {}).get(group, []):
            if book not in seen:
                books.append(book)
                seen.add(book)
            if len(books) == count:
                return books
    return books  # May return fewer if not enough globally

# Suggestion logic
if st.button("Suggest Genre and Books"):
    st.write(f"Thanks, {name or 'reader'}! Based on your preferences:")

    suggestions = set()
    age_group = get_age_group(age)

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
        books = get_books_for_genre(genre, age_group, count=5)
        st.write(f"Recommended for your age group ({age_group.title()}):")
        for book in books:
            st.write(f"- {book}")
