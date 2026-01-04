import streamlit as st
import random

# --- CONFIG ---
st.set_page_config(page_title="Logic Hacker", layout="centered")

# --- ULTRA MINIMALIST CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; color: #000000; }
    header, footer, .stDeployButton { visibility: hidden; }
    
    .app-title {
        font-size: 1.2rem; font-weight: 700; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        margin-top: 20px; padding-bottom: 20px; border-bottom: 1px solid #000000;
    }
    .mission-header {
        text-align: center; font-size: 0.7rem; letter-spacing: 2px;
        margin-top: 20px; text-transform: uppercase; font-weight: 700;
    }
    .quiz-card {
        margin: 30px 0; padding: 50px 10px;
        border: 1px solid #000000; text-align: center;
    }
    .word-main { font-size: 2rem; font-weight: 700; text-transform: none; }
    
    .stButton>button {
        width: 100% !important; background-color: #000000 !important;
        color: #FFFFFF !important; border: 1px solid #000000 !important;
        border-radius: 0px !important; padding: 16px !important;
        font-size: 0.85rem !important; text-transform: uppercase;
        letter-spacing: 1px; margin-bottom: 8px;
    }
    .stButton>button:hover { background-color: #FFFFFF !important; color: #000000 !important; }
    
    /* Input polje za kucanje (Letter Hunter) */
    .stTextInput input {
        border-radius: 0px !important; border: 1px solid #000 !important;
        text-align: center; font-size: 1.2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SVEOBUHVATNA BAZA (1000 REČI - Primer kategorizacije) ---
# U pravoj aplikaciji ovde ide svih 1000 reči podeljenih u liste
words_office = [
    {"de": "die Verantwortung", "sr": "odgovornost", "ex": "Ich trage die ___."},
    {"de": "besprechen", "sr": "prodiskutovati", "ex": "Wir müssen das ___."},
    {"de": "die Kündigung", "sr": "otkaz", "ex": "Er hat die ___ erhalten."},
    {"de": "verhandeln", "sr": "pregovarati", "ex": "Wir ___ über das Gehalt."}
]

words_life = [
    {"de": "obwohl", "sr": "iako", "ex": "Ich komme, ___ ja ich müde bin."},
    {"de": "trotzdem", "sr": "uprkos tome", "ex": "Es regnet, ___ gehe ich raus."},
    {"de": "anstrengend", "sr": "naporno", "ex": "Der Tag war sehr ___."}
]

# --- LOGIKA ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'mission' not in st.session_state: st.session_state.mission = "OFFICE CHAOS"

def reset_quiz():
    st.session_state.current_q = random.choice(words_office + words_life)
    # Generisanje opcija
    correct = st.session_state.current_q['sr']
    all_sr = [w['sr'] for w in (words_office + words_life)]
    others = list(set([s for s in all_sr if s != correct]))
    st.session_state.options = random.sample(others, 3) + [correct]
    random.shuffle(st.session_state.options)

if 'current_q' not in st.session_state:
    reset_quiz()

# --- UI ---
st.markdown("<div class='app-title'>Logic Hacker</div>", unsafe_allow_html=True)

# Menu za izbor misije (Kvizova)
mission_choice = st.selectbox("IZABERI MISIJU:", ["OFFICE CHAOS", "LETTER HUNTER", "SENTENCE BUILDER"])

if mission_choice != st.session_state.mission:
    st.session_state.mission = mission_choice
    reset_quiz()
    st.rerun()

st.markdown(f"<div class='mission-header'>{st.session_state.mission} | XP: {st.session_state.xp}</div>", unsafe_allow_html=True)

# --- MOD 1: OFFICE CHAOS (Pogađanje reči) ---
if st.session_state.mission == "OFFICE CHAOS":
    st.markdown(f"""
        <div class='quiz-card'>
            <div style='font-size:0.7rem; opacity:0.5;'>PREVEDI</div>
            <div class='word-main'>{st.session_state.current_q['de']}</div>
        </div>
        """, unsafe_allow_html=True)

    for opt in st.session_state.options:
        if st.button(opt):
            if opt == st.session_state.current_q['sr']:
                st.session_state.xp += 10
                reset_quiz()
                st.rerun()
            else:
                st.toast("Falsch!")

# --- MOD 2: LETTER HUNTER (Kucanje reči - Spelling) ---
elif st.session_state.mission == "LETTER HUNTER":
    st.markdown(f"""
        <div class='quiz-card'>
            <div style='font-size:0.7rem; opacity:0.5;'>UPIŠI NEMAČKU REČ</div>
            <div class='word-main'>{st.session_state.current_q['sr']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    user_input = st.text_input("ODGOVOR:", key="hunter_input").strip()
    if st.button("PROVERI"):
        if user_input.lower() == st.session_state.current_q['de'].lower():
            st.session_state.xp += 20
            reset_quiz()
            st.rerun()
        else:
            st.error(f"Nije tačno. Tačno je: {st.session_state.current_q['de']}")

# --- MOD 3: SENTENCE BUILDER (Logika rečenice) ---
elif st.session_state.mission == "SENTENCE BUILDER":
    example_sentence = st.session_state.current_q['ex']
    missing_word = st.session_state.current_q['de']
    
    st.markdown(f"""
        <div class='quiz-card'>
            <div style='font-size:0.7rem; opacity:0.5;'>DOPUNI REČENICU</div>
            <div class='word-main' style='font-size:1.4rem;'>{example_sentence}</div>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button(missing_word):
        st.session_state.xp += 15
        reset_quiz()
        st.rerun()
    if st.button("pokušaj nešto drugo"):
        st.toast("To ne ide tu.")

# Donji meni
st.write("---")
if st.button("SLEDEĆA REČ ➔"):
    reset_quiz()
    st.rerun()
