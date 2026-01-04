import streamlit as st

st.set_page_config(page_title="Logic Hacker Pro", layout="centered")

# --- CUSTOM STYLING (Boje i Fontovi) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;700&display=swap');

    .main { 
        background-color: #0F1116; 
        color: #E0E0E0; 
        font-family: 'Lexend', sans-serif;
    }
    
    .main-title {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        margin-top: 15px;
        border-left: 5px solid #00f2fe;
    }

    .stTextInput>div>div>input {
        background-color: #1A1D24;
        color: #FFFFFF;
        border: 1px solid #333;
        border-radius: 10px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #00f2fe !important;
        color: #000 !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- MASIVNA BAZA PODATAKA ---
# Ubacio sam tvoju listu i formatirao je za pretragu
raw_data = {
    "Anfang": "Početak", "Anforderung": "Zahtev", "Antwort": "Odgovor", "Arbeit": "Rad",
    "Aufgabe": "Zadatak", "Bedarf": "Potreba", "Bedeutung": "Značenje", "Bedingung": "Uslov",
    "Beispiel": "Primer", "Beitrag": "Doprinos", "Bereich": "Oblast", "Bewegung": "Kretanje",
    "Beziehung": "Odnos", "Chance": "Šansa", "Einfluss": "Uticaj", "Ende": "Kraj",
    "Entscheidung": "Odluka", "Entwicklung": "Razvoj", "Erfahrung": "Iskustvo", "Erfolg": "Uspeh",
    "Ergebnis": "Rezultat", "Faktor": "Faktor", "Fall": "Slučaj", "Fehler": "Greška",
    "Folge": "Posledica", "Form": "Forma", "Fortschritt": "Napredak", "Frage": "Pitanje",
    "Grenze": "Granica", "Grund": "Razlog", "Hinweis": "Napomena", "Idee": "Ideja",
    "Inhalt": "Sadržaj", "Jahr": "Godina", "Kenntnis": "Znanje", "Meinung": "Mišljenje",
    "Moeglichkeit": "Mogućnost", "Nachteil": "Nedostatak", "Nutzen": "Korist", "Plan": "Plan",
    "Problem": "Problem", "Prozess": "Proces", "Qualitaet": "Kvalitet", "Rahmen": "Okvir",
    "Regel": "Pravilo", "Risiko": "Rizik", "Rolle": "Uloga", "Schritt": "Korak",
    "Situation": "Situacija", "Teil": "Deo", "Thema": "Tema", "Unterschied": "Razlika",
    "Ursache": "Uzrok", "Veraenderung": "Promena", "Verantwortung": "Odgovornost", "Vergleich": "Poređenje",
    "Verhalten": "Ponašanje", "Voraussetzung": "Preduslov", "Vorteil": "Prednost", "Weg": "Put",
    "Wert": "Vrednost", "Wirkung": "Dejstvo", "Zeit": "Vreme", "Ziel": "Cilj",
    "arbeiten": "Raditi", "bedeuten": "Značiti", "beginnen": "Početi", "besprechen": "Dogovoriti",
    "denken": "Misliti", "entscheiden": "Odlučiti", "erklären": "Objasniti", "verstehen": "Razumeti",
    "wichtig": "Važno", "schnell": "Brzo", "einfach": "Jednostavno", "klar": "Jasno"
}

# --- UI ---
st.markdown("<h1 class='main-title'>LOGIC HACKER</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["DEKODIRAJ (DE)", "PREVEDI (SRB)"])

with tab1:
    search_de = st.text_input("Unesi nemačku reč:", placeholder="npr. Entscheidung...", key="de")
    if search_de:
        found = False
        for de, srb in raw_data.items():
            if de.lower() in search_de.lower():
                st.markdown(f"""
                <div class='result-card'>
                    <h3 style='margin:0; color:#00f2fe;'>{de}</h3>
                    <p style='font-size:1.2rem; margin-top:5px;'>{srb}</p>
                </div>
                """, unsafe_allow_html=True)
                found = True
        if not found: st.info("Reč nije u bazi.")

with tab2:
    search_srb = st.text_input("Unesi srpski pojam:", placeholder="npr. Odluka...", key="srb")
    if search_srb:
        found = False
        for de, srb in raw_data.items():
            if search_srb.lower() in srb.lower():
                st.markdown(f"""
                <div class='result-card'>
                    <h3 style='margin:0; color:#00f2fe;'>{de}</h3>
                    <p style='font-size:1.2rem; margin-top:5px;'>Prevod za: {srb}</p>
                </div>
                """, unsafe_allow_html=True)
                found = True
        if not found: st.info("Pojam nije u bazi.")
