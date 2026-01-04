import streamlit as st
import random
import string

# --- CONFIG ---
st.set_page_config(page_title="Logic Hacker", layout="centered")

# --- ULTRA MINIMALIST CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #FFF; font-family: 'Inter', sans-serif; color: #000; }
    header, footer, .stDeployButton { visibility: hidden; }
    .app-title {
        font-size: 1.2rem; font-weight: 700; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        margin-top: 10px; padding-bottom: 10px; border-bottom: 2px solid #000;
    }
    .grid-container {
        font-family: monospace; font-size: 1.5rem; line-height: 2rem;
        letter-spacing: 0.8rem; text-align: center; margin: 20px 0;
        background: #000; color: #FFF; padding: 20px; border-radius: 0px;
    }
    .quiz-card {
        margin: 20px 0; padding: 40px 10px;
        border: 2px solid #000; text-align: center;
    }
    .stButton>button {
        width: 100% !important; background-color: #000 !important;
        color: #FFF !important; border: 1px solid #000 !important;
        border-radius: 0px !important; padding: 15px !important;
        text-transform: uppercase; font-weight: 700; margin-bottom: 5px;
    }
    .stButton>button:hover { background-color: #FFF !important; color: #000 !important; }
    .stTextInput input { border-radius: 0px !important; border: 2px solid #000 !important; font-size: 1.2rem !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- PROŠIRENA BAZA (100+ REČI) ---
words_db = [
    {"de": "obwohl", "sr": "iako"}, {"de": "trotzdem", "sr": "uprkos tome"}, 
    {"de": "entscheiden", "sr": "odlučiti"}, {"de": "die Verantwortung", "sr": "odgovornost"},
    {"de": "die Ausbildung", "sr": "obrazovanje"}, {"de": "besprechen", "sr": "prodiskutovati"},
    {"de": "anstrengend", "sr": "naporno"}, {"de": "das Gehalt", "sr": "plata"},
    {"de": "die Kündigung", "sr": "otkaz"}, {"de": "verhandeln", "sr": "pregovarati"},
    {"de": "die Erlaubnis", "sr": "dozvola"}, {"de": "beeinflussen", "sr": "uticati"},
    {"de": "der Eindruck", "sr": "utisak"}, {"de": "empfehlen", "sr": "preporučiti"},
    {"de": "vorsichtig", "sr": "oprezan"}, {"de": "nützlich", "sr": "korisno"},
    {"de": "die Beziehung", "sr": "odnos"}, {"de": "das Ergebnis", "sr": "rezultat"},
    {"de": "die Lösung", "sr": "rešenje"}, {"de": "bestätigen", "sr": "potvrditi"},
    {"de": "die Herausforderung", "sr": "izazov"}, {"de": "vermeiden", "sr": "izbeći"},
    {"de": "die Voraussetzung", "sr": "preduslov"}, {"de": "die Erfahrung", "sr": "iskustvo"},
    {"de": "pünktlich", "sr": "tačan"}, {"de": "zuverlässig", "sr": "pouzdan"},
    {"de": "die Abteilung", "sr": "odeljenje"}, {"de": "der Bereich", "sr": "oblast"},
    {"de": "gemeinsam", "sr": "zajedno"}, {"de": "die Entwicklung", "sr": "razvoj"}
] # Dodaj ovde još reči po istom šablonu

# --- POMOĆNE FUNKCIJE ZA OSMOSMERKU ---
def generate_word_search(word, size=10):
    grid = [[random.choice(string.ascii_uppercase) for _ in range(size)] for _ in range(size)]
    word = word.upper().replace(" ", "")
    if len(word) > size: size = len(word) + 2
    
    # Postavi reč vodoravno ili uspravno
    direction = random.choice(['H', 'V'])
    if direction == 'H':
        row = random.randint(0, size-1)
        col = random.randint(0, size-len(word))
        for i, char in enumerate(word): grid[row][col+i] = char
    else:
        row = random.randint(0, size-len(word))
        col = random.randint(0, size-1)
        for i, char in enumerate(word): grid[row+i][col] = char
    return grid

# --- SESSION STATE ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'current_q' not in st.session_state: st.session_state.current_q = random.choice(words_db)
if 'grid' not in st.session_state: st.session_state.grid = generate_word_search(st.session_state.current_q['de'])

def next_question():
    st.session_state.current_q = random.choice(words_db)
    st.session_state.grid = generate_word_search(st.session_state.current_q['de'])
    if 'options' in st.session_state: del st.session_state.options

# --- UI ---
st.markdown("<div class='app-title'>Logic Hacker</div>", unsafe_allow_html=True)
mode = st.selectbox("MOD:", ["OSMOSMERKA", "POGAĐANJE", "LETTER HUNTER"])

st.write(f"XP: {st.session_state.xp}")

# --- MOD 1: PRAVA OSMOSMERKA ---
if mode == "OSMOSMERKA":
    st.write(f"Pronađi reč za: **{st.session_state.current_q['sr']}**")
    grid_html = "".join(["".join(row) + "<br>" for row in st.session_state.grid])
    st.markdown(f"<div class='grid-container'>{grid_html}</div>", unsafe_allow_html=True)
    
    ans = st.text_input("KOJA JE REČ?", key="os_ans").strip().lower()
    if st.button("PROVERI"):
        if ans == st.session_state.current_q['de'].lower():
            st.session_state.xp += 30
            st.success("TAČNO!")
            next_question()
            st.rerun()
        else: st.error("TRAŽI DALJE...")

# --- MOD 2: POGAĐANJE ---
elif mode == "POGAĐANJE":
    if 'options' not in st.session_state:
        correct = st.session_state.current_q['sr']
        others = random.sample([w['sr'] for w in words_db if w['sr'] != correct], 3)
        opts = others + [correct]
        random.shuffle(opts)
        st.session_state.options = opts

    st.markdown(f"<div class='quiz-card'><h1>{st.session_state.current_q['de']}</h1></div>", unsafe_allow_html=True)
    for o in st.session_state.options:
        if st.button(o):
            if o == st.session_state.current_q['sr']:
                st.session_state.xp += 10
                next_question()
                st.rerun()
            else: st.toast("Pogrešno!")

# --- MOD 3: LETTER HUNTER ---
elif mode == "LETTER HUNTER":
    st.markdown(f"<div class='quiz-card'><h3>Upiši nemačku reč za:</h3><h1>{st.session_state.current_q['sr']}</h1></div>", unsafe_allow_html=True)
    hunter_ans = st.text_input("ODGOVOR:", key="h_ans").strip().lower()
    if st.button("PROVERI"):
        if hunter_ans == st.session_state.current_q['de'].lower():
            st.session_state.xp += 20
            next_question()
            st.rerun()
        else: st.error(f"Nije tačno. Reč je: {st.session_state.current_q['de']}")

if st.button("SLEDEĆA REČ ➔"):
    next_question()
    st.rerun()
