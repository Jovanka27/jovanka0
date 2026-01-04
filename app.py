import streamlit as st
import random

# Postavke stranice
st.set_page_config(page_title="Logic Hacker", layout="centered")

# --- MINIMALIST BLACK & WHITE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');

    /* Osnovna pozadina i font */
    .stApp {
        background-color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        color: #000000;
    }

    /* Sakrivanje Streamlit elemenata */
    header, footer, .stDeployButton { visibility: hidden; }

    /* Naslov */
    .app-title {
        font-size: 1.5rem;
        font-weight: 700;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: 40px;
        border-bottom: 2px solid #000000;
        padding-bottom: 10px;
        color: #000000;
    }

    /* Kartica za kviz */
    .quiz-card {
        margin: 50px 0;
        padding: 40px 20px;
        border: 1px solid #000000;
        text-align: center;
        background: #FFFFFF;
    }

    .word-main {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 10px;
        color: #000000;
    }

    /* Button stilizacija - Crna pozadina, bela slova */
    .stButton>button {
        width: 100%;
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 0px !important;
        padding: 15px !important;
        font-size: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s;
        margin-bottom: 10px;
    }

    .stButton>button:hover {
        background-color: #333333 !important;
    }

    /* Statistika */
    .stat-text {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-align: center;
        color: #000000;
    }

    /* Feedback poruke */
    .stAlert {
        border-radius: 0px !important;
        border: 1px solid #000000 !important;
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAZA PODATAKA (1000 REČI - Primer) ---
# Tipovi: N (Nomen), V (Verb), A (Adj)
words_db = [
    {"de": "die Verantwortung", "sr": "odgovornost", "type": "N"},
    {"de": "entscheiden", "sr": "odlučiti", "type": "V"},
    {"de": "obwohl", "sr": "iako", "type": "O"},
    {"de": "anstrengend", "sr": "naporno", "type": "A"},
    {"de": "das Gehalt", "sr": "plata", "type": "N"},
    {"de": "besprechen", "sr": "prodiskutovati", "type": "V"},
    {"de": "fleißig", "sr": "vredan", "type": "A"},
    {"de": "trotzdem", "sr": "uprkos tome", "type": "O"}
]

# --- LOGIKA APLIKACIJE ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(words_db)

# --- UI ---
st.markdown("<div class='app-title'>Logic Hacker Pro</div>", unsafe_allow_html=True)
st.write("")
st.markdown(f"<div class='stat-text'>NIVO: B1 &nbsp; | &nbsp; POENI: {st.session_state.xp}</div>", unsafe_allow_html=True)

# Centralna kartica
st.markdown(f"""
    <div class='quiz-card'>
        <div style='font-size: 0.7rem; letter-spacing: 2px; margin-bottom: 10px;'>DEUTSCH</div>
        <div class='word-main'>{st.session_state.current_word['de']}</div>
    </div>
    """, unsafe_allow_html=True)

# Generisanje opcija (tačna + 3 nasumične)
correct_answer = st.session_state.current_word['sr']
if 'options' not in st.session_state:
    others = [w['sr'] for w in words_db if w['sr'] != correct_answer]
    st.session_state.options = random.sample(others, 3) + [correct_answer]
    random.shuffle(st.session_state.options)

# Dugmići za odgovore
for option in st.session_state.options:
    if st.button(option):
        if option == correct_answer:
            st.session_state.xp += 10
            # Reset za sledeću reč
            st.session_state.current_word = random.choice(words_db)
            # Čišćenje opcija da bi se generisale nove za sledeću reč
            del st.session_state.options
            st.rerun()
        else:
            st.error("POGREŠNO. POKUŠAJ PONOVO.")

# Pomoćne opcije na dnu
st.write("")
if st.button("PRESKOČI REČ ➔", key="skip"):
    st.session_state.current_word = random.choice(words_db)
    if 'options' in st.session_state: del st.session_state.options
    st.rerun()

# --- OSMOSMERKA IDEJA (Minimalistička) ---
with st.sidebar:
    st.markdown("### INFO")
    st.write("Cilj: 2400 reči.")
    st.write("---")
    st.write("USKORO: Osmosmerka mod.")
    if st.button("RESET XP"):
        st.session_state.xp = 0
        st.rerun()
