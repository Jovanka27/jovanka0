import streamlit as st
import random
import string

# --- CONFIG ---
st.set_page_config(page_title="Logic Hacker", layout="centered")

# --- CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #FFF; font-family: 'Inter', sans-serif; color: #000; }
    header, footer, .stDeployButton { visibility: hidden; }
    
    .app-title {
        font-size: 1.2rem; font-weight: 700; text-align: center;
        text-transform: uppercase; letter-spacing: 5px;
        margin-top: 5px; padding-bottom: 10px; border-bottom: 2px solid #000;
    }
    
    /* Grid styling za pravu osmosmerku */
    .grid-table {
        margin: auto; border-collapse: collapse; font-family: monospace;
    }
    .grid-cell {
        width: 25px; height: 25px; border: 1px solid #EEE;
        text-align: center; font-size: 1rem; font-weight: bold;
    }
    .coords { color: #888; font-size: 0.6rem; }

    .quiz-card {
        margin: 15px 0; padding: 20px;
        border: 2px solid #000; text-align: center;
    }

    .stButton>button {
        width: 100% !important; background-color: #000 !important;
        color: #FFF !important; border: 1px solid #000 !important;
        border-radius: 0px !important; padding: 12px !important;
        text-transform: uppercase; font-weight: 700; margin-bottom: 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAZA ---
words_db = [
    {"de": "OBWOHL", "sr": "iako"}, {"de": "TROTZDEM", "sr": "uprkos tome"},
    {"de": "ENTSCHEIDEN", "sr": "odlučiti"}, {"de": "GEHALT", "sr": "plata"},
    {"de": "ERGEBNIS", "sr": "rezultat"}, {"de": "LOESUNG", "sr": "rešenje"}
]

# --- OSMOSMERKA ENGINE ---
def generate_fixed_grid(word, size=10):
    grid = [[random.choice(string.ascii_uppercase) for _ in range(size)] for _ in range(size)]
    direction = random.choice(['H', 'V'])
    if direction == 'H':
        r, c = random.randint(0, size-1), random.randint(0, size-len(word))
        for i, char in enumerate(word): grid[r][c+i] = char
        pos = f"Red {r+1}"
    else:
        r, c = random.randint(0, size-len(word)), random.randint(0, size-1)
        for i, char in enumerate(word): grid[r+i][c] = char
        pos = f"Kolona {c+1}"
    return grid, pos

# --- SESSION ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(words_db)
    st.session_state.grid, st.session_state.pos = generate_fixed_grid(st.session_state.current_q['de'])

def refresh():
    st.session_state.current_q = random.choice(words_db)
    st.session_state.grid, st.session_state.pos = generate_fixed_grid(st.session_state.current_q['de'])
    st.rerun()

# --- UI ---
st.markdown("<div class='app-title'>Logic Hacker</div>", unsafe_allow_html=True)
st.write(f"XP: {st.session_state.xp}")

st.markdown(f"<div class='quiz-card'>PRONAĐI: <b>{st.session_state.current_q['de']}</b><br>(Prevod: {st.session_state.current_q['sr']})</div>", unsafe_allow_html=True)

# Prikaz mreže sa brojevima redova i kolona (koordinate)
cols_header = "&nbsp;&nbsp;&nbsp;&nbsp;" + "&nbsp;".join([str(i+1).zfill(1) for i in range(10)])
st.markdown(f"<code style='color:red;'>{cols_header}</code>", unsafe_allow_html=True)

for i, row in enumerate(st.session_state.grid):
    row_str = f"<span style='color:red;'>{i+1}</span>&nbsp;&nbsp; " + " ".join(row)
    st.markdown(f"<code>{row_str}</code>", unsafe_allow_html=True)

st.write("---")

# Pravi mod za "pronalaženje"
st.write("Gde se nalazi reč?")
answer = st.radio("Izaberi lokaciju:", [st.session_state.pos, "Red 11", "Kolona 12", "Red 0"], index=None)

if st.button("POTVRDI PRONALAZAK"):
    if answer == st.session_state.pos:
        st.session_state.xp += 50
        st.success("BRAVO! Pronašao si je!")
        refresh()
    else:
        st.error("Nije tu, gledaj pažljivije!")

if st.button("SLEDEĆA ➔"):
    refresh()
