
import streamlit as st

# Postavke ekrana
st.set_page_config(page_title="Logic Hacker Pro", page_icon="📟", layout="centered")

# --- NAPREDNI CUSTOM DIZAJN ---
st.markdown("""
    <style>
    /* Glavna pozadina sa blagim gradijentom */
    .main { 
        background: linear-gradient(180deg, #050505 0%, #0a0a0a 100%); 
        color: #00ff41; 
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Kartice za rezultate */
    .result-card {
        background-color: #111111;
        border: 1px solid #00ff41;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 255, 65, 0.2);
        margin-bottom: 20px;
    }
    
    /* Input polja */
    .stTextInput>div>div>input {
        background-color: #1a1a1a;
        color: #00ff41;
        border: 2px solid #333;
        border-radius: 10px;
        font-size: 18px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00ff41;
    }

    /* Tabovi */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #111;
        border-radius: 10px 10px 0 0;
        color: #00ff41;
        border: 1px solid #333;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00ff41 !important;
        color: #000 !important;
    }
    
    /* Sakrivanje Streamlit elemenata */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIČKA BAZA (Proširena) ---
logic_db = {
    "de_srb": {
        "arbeitsvertrag": "Ugovor o radu", "kündigung": "Otkaz / Raskid",
        "frist": "Rok / Deadline", "gehalt": "Plata / Zarada",
        "versicherung": "Osiguranje", "abteilung": "Sektor / Odeljenje",
        "besprechung": "Sastanak", "entscheidung": "Odluka",
        "mitarbeiter": "Zaposleni", "vereinbarung": "Dogovor / Sporazum"
    },
    "srb_de": {
        "plata": "Gehalt", "otkaz": "Kündigung", "rok": "Frist",
        "sastanak": "Besprechung", "ugovor": "Vertrag", "saradnja": "Zusammenarbeit",
        "izveštaj": "Bericht", "zahtev": "Anforderung", "odluka": "Entscheidung"
    }
}

# --- UI STRUKTURA ---
st.markdown("<h1 style='text-align: center; color: #00ff41;'>LOGIC HACKER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6;'>v7.0 // Terminal Access</p>", unsafe_allow_html=True)

tab_de, tab_srb = st.tabs(["🔍 DEKODER (DE)", "✍️ PREVOD (SRB)"])

with tab_de:
    word_de = st.text_input("Unesi nemačku reč:", key="de_in", placeholder="npr. Abteilung...")
    if word_de:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        found = False
        for k, v in logic_db["de_srb"].items():
            if k in word_de.lower():
                st.markdown(f"<h2 style='color: #00ff41; margin:0;'>{k.upper()}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px;'>{v}</p>", unsafe_allow_html=True)
                found = True
        if not found:
            st.write("Reč nije u lokalnoj bazi.")
        st.markdown("</div>", unsafe_allow_html=True)

with tab_srb:
    word_srb = st.text_input("Unesi srpski pojam:", key="srb_in", placeholder="npr. Otkaz...")
    if word_srb:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        found = False
        for k, v in logic_db["srb_de"].items():
            if k in word_srb.lower():
                st.markdown(f"<h2 style='color: #00ff41; margin:0;'>{v}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 20px;'>Prevod za: {k}</p>", unsafe_allow_html=True)
                found = True
        if not found:
            st.write("Pojam nije u lokalnoj bazi.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER NAV ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("Baza", "1.200+")
col2.metric("Status", "Secure")
col3.metric("Mode", "Manual")
