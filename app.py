import streamlit as st
import random

# --- CONFIG ---
st.set_page_config(page_title="Logic Hacker", layout="centered")

# --- CLEAN BLACK & WHITE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; color: #000000; }
    header, footer, .stDeployButton { visibility: hidden; }
    
    .app-title {
        font-size: 1.2rem; font-weight: 700; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        margin-top: 10px; padding-bottom: 10px; border-bottom: 2px solid #000;
    }
    
    .quiz-card {
        margin: 20px 0; padding: 40px 10px;
        border: 2px solid #000; text-align: center;
    }

    .word-main { font-size: 2rem; font-weight: 700; }

    /* Fix za dugmiće da ne lete po ekranu */
    .stButton>button {
        width: 100% !important; background-color: #000 !important;
        color: #FFF !important; border: 1px solid #000 !important;
        border-radius: 0px !important; padding: 15px !important;
        text-transform: uppercase; font-weight: 700; margin-bottom: 10px !important;
    }
    .stButton>button:hover { background-color: #FFF !important; color: #000 !important; }

    /* Fix za input polje */
    .stTextInput input {
        border-radius: 0px !important; border: 2px solid #000 !important;
        height: 50px !important; font-size: 1.1rem !important; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MASIVNA BAZA (Sve reči su ovde) ---
words_db = [
    {"de": "obwohl", "sr": "iako"}, {"de": "trotzdem", "sr": "uprkos tome"}, {"de": "entscheiden", "sr": "odlučiti"},
    {"de": "Verantwortung", "sr": "odgovornost"}, {"de": "Ausbildung", "sr": "obrazovanje"}, {"de": "besprechen", "sr": "prodiskutovati"},
    {"de": "anstrengend", "sr": "naporno"}, {"de": "Gehalt", "sr": "plata"}, {"de": "Kündigung", "sr": "otkaz"},
    {"de": "verhandeln", "sr": "pregovarati"}, {"de": "Erlaubnis", "sr": "dozvola"}, {"de": "beeinflussen", "sr": "uticati"},
    {"de": "Eindruck", "sr": "utisak"}, {"de": "empfehlen", "sr": "preporučiti"}, {"de": "vorsichtig", "sr": "oprezan"},
    {"de": "nützlich", "sr": "korisno"}, {"de": "Beziehung", "sr": "odnos"}, {"de": "Ergebnis", "sr": "rezultat"},
    {"de": "Lösung", "sr": "rešenje"}, {"de": "bestätigen", "sr": "potvrditi"}, {"de": "Herausforderung", "sr": "izazov"},
    {"de": "vermeiden", "sr": "izbeći"}, {"de": "Voraussetzung", "sr": "preduslov"}, {"de": "Erfahrung", "sr": "iskustvo"},
    {"de": "pünktlich", "sr": "tačan"}, {"de": "zuverlässig", "sr": "pouzdan"}, {"de": "Abteilung", "sr": "odeljenje"},
    {"de": "Bereich", "sr": "oblast"}, {"de": "gemeinsam", "sr": "zajedno"}, {"de": "Entwicklung", "sr": "razvoj"}
]

# --- LOGIKA BEZ GREŠAKA ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'history' not in st.session_state: st.session_state.history = []

def next_question():
    # Uzmi reči koje nisu bile skoro
    available = [w for w in words_db if w['de'] not in st.session_state.history]
    if not available:
        st.session_state.history = []
        available = words_db
    
    q = random.choice(available)
    st.session_state.history.append(q['de'])
    if len(st.session_state.history) > 15: st.session_state.history.pop(0)
    
    st.session_state.current_q = q
    # Generisanje 4 opcije za pogađanje
    correct = q['sr']
    wrong = random.sample([w['sr'] for w in words_db if w['sr'] != correct], 3)
    opts = wrong + [correct]
    random.shuffle(opts)
    st.session_state.options = opts

if 'current_q' not in st.session_state:
    next_question()

# --- RENDER ---
st.markdown("<div class='app-title'>Logic Hacker</div>", unsafe_allow_html=True)

mode = st.selectbox("IZABERI MOD:", ["POGAĐANJE", "LETTER HUNTER"])
st.markdown(f"<p style='text-align:center; font-weight:bold; margin-top:10px;'>XP: {st.session_state.xp}</p>", unsafe_allow_html=True)

# MOD 1: POGAĐANJE (Sređen raspored)
if mode == "POGAĐANJE":
    st.markdown(f"""
        <div class='quiz-card'>
            <div style='font-size:0.8rem; opacity:0.6; margin-bottom:10px;'>ŠTA ZNAČI:</div>
            <div class='word-main'>{st.session_state.current_q['de']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    for opt in st.session_state.options:
        if st.button(opt, key=opt):
            if opt == st.session_state.current_q['sr']:
                st.session_state.xp += 10
                next_question()
                st.rerun()
            else:
                st.toast("Pokušaj ponovo!")

# MOD 2: LETTER HUNTER (Fix za eror)
elif mode == "LETTER HUNTER":
    st.markdown(f"""
        <div class='quiz-card'>
            <div style='font-size:0.8rem; opacity:0.6; margin-bottom:10px;'>UPIŠI NEMAČKU REČ:</div>
            <div class='word-main'>{st.session_state.current_q['sr']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    ans = st.text_input("ODGOVOR:", key="ans_input").strip().lower()
    if st.button("PROVERI"):
        if ans == st.session_state.current_q['de'].lower():
            st.session_state.xp += 20
            next_question()
            st.rerun()
        else:
            st.error(f"Netačno! Reč je: {st.session_state.current_q['de']}")

st.write("---")
if st.button("SLEDEĆA REČ ➔"):
    next_question()
    st.rerun()
