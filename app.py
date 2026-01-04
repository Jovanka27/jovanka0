import streamlit as st
import random

# Mobile-First konfiguracija
st.set_page_config(page_title="Logic Hacker Pro", page_icon="🇩🇪", layout="centered")

# --- PREMIUM MOBILE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    .stApp { background-color: #08090A; font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .mobile-header {
        text-align: center; padding: 25px 0;
        background: linear-gradient(180deg, #1A1D24 0%, #08090A 100%);
        border-bottom: 1px solid #30363D; margin-bottom: 20px;
    }
    .main-title {
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 2.2rem; font-weight: 800; margin: 0;
    }
    .word-card {
        background: #12141D; border-radius: 16px; padding: 20px;
        margin-bottom: 12px; border: 1px solid #1F222C;
    }
    .de-text { color: #FFFFFF; font-size: 1.4rem; font-weight: 700; }
    .srb-text { color: #94A3B8; font-size: 1.1rem; }
    
    .pill {
        display: inline-block; padding: 4px 12px; border-radius: 20px;
        font-size: 0.7rem; font-weight: 800; margin-bottom: 10px;
    }
    .nomen { background: rgba(34, 197, 94, 0.15); color: #4ade80; }
    .verb { background: rgba(168, 85, 247, 0.15); color: #c084fc; }
    .adj { background: rgba(234, 179, 8, 0.15); color: #facc15; }
    
    .stTextInput input { height: 55px !important; border-radius: 15px !important; font-size: 16px !important; }
    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- BAZA PODATAKA (Primer strukture za 1000 reči) ---
raw_data = {
    "die Abteilung": ["odeljenje", "N"], "die Anzeige": ["oglas", "N"], "die Ausbildung": ["obrazovanje", "N"],
    "die Bewerbung": ["prijava", "N"], "das Gehalt": ["plata", "N"], "die Verantwortung": ["odgovornost", "N"],
    "die Entscheidung": ["odluka", "N"], "die Erfahrung": ["iskustvo", "N"], "die Möglichkeit": ["mogućnost", "N"],
    "die Zukunft": ["budućnost", "N"], "das Ergebnis": ["rezultat", "N"], "die Meinung": ["mišljenje", "N"],
    "besprechen": ["prodiskutovati", "V"], "entscheiden": ["odlučiti", "V"], "kündigen": ["otkazati", "V"],
    "verhandeln": ["pregovarati", "V"], "empfehlen": ["preporučiti", "V"], "erklären": ["objasniti", "V"],
    "versprechen": ["obećati", "V"], "verschieben": ["odložiti", "V"], "übernehmen": ["preuzeti", "V"],
    "abhängig": ["zavisan", "A"], "anstrengend": ["naporno", "A"], "erfolgreich": ["uspešan", "A"],
    "vorsichtig": ["oprezan", "A"], "zufrieden": ["zadovoljan", "A"], "wichtig": ["važno", "A"],
    "obwohl": ["iako", "O"], "trotzdem": ["uprkos tome", "O"], "vielleicht": ["možda", "O"]
}

# --- UI APP ---
st.markdown("<div class='mobile-header'><h1 class='main-title'>LOGIC HACKER</h1></div>", unsafe_allow_html=True)

menu = st.selectbox("Izaberi mod:", ["Rečnik", "Blic Test (Quiz)"])

if menu == "Rečnik":
    tab1, tab2 = st.tabs(["🇩🇪 Nemački", "🇷🇸 Srpski"])
    
    with tab1:
        q_de = st.text_input("", placeholder="Traži reč...", key="de")
        if q_de:
            for de, info in raw_data.items():
                if q_de.lower() in de.lower():
                    p_cl = {"N":"nomen","V":"verb","A":"adj"}.get(info[1], "other")
                    st.markdown(f"<div class='word-card'><span class='pill {p_cl}'>{info[1]}</span><div class='de-text'>{de}</div><div class='srb-text'>{info[0]}</div></div>", unsafe_allow_html=True)
                    
    with tab2:
        q_sr = st.text_input("", placeholder="Traži prevod...", key="sr")
        if q_sr:
            for de, info in raw_data.items():
                if q_sr.lower() in info[0].lower():
                    p_cl = {"N":"nomen","V":"verb","A":"adj"}.get(info[1], "other")
                    st.markdown(f"<div class='word-card'><span class='pill {p_cl}'>{info[1]}</span><div class='de-text'>{de}</div><div class='srb-text'>{info[0]}</div></div>", unsafe_allow_html=True)

elif menu == "Blic Test (Quiz)":
    st.markdown("### Testiraj se! 🧠")
    if 'quiz_word' not in st.session_state:
        st.session_state.quiz_word = random.choice(list(raw_data.keys()))
        
    word = st.session_state.quiz_word
    st.markdown(f"<div class='word-card' style='text-align:center;'><div class='de-text' style='font-size:2rem;'>{word}</div></div>", unsafe_allow_html=True)
    
    if st.button("Prikaži odgovor"):
        st.success(f"Prevod: {raw_data[word][0]}")
    
    if st.button("Sledeća reč ➔"):
        st.session_state.quiz_word = random.choice(list(raw_data.keys()))
        st.rerun()

st.sidebar.markdown("### 🇩🇪 B1 Napredak")
st.sidebar.info(f"Trenutno u bazi: {len(raw_data)} reči")
