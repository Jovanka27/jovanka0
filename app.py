import streamlit as st

st.set_page_config(page_title="Logic Hacker Pro", layout="centered")

# --- PREMIUM DIZAJN ---
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
        margin-bottom: 10px;
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
        font-weight: bold;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- KOMPLETNA BAZA (Sve tvoje reči) ---
# Format: "Nemački": "Srpski"
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
    "wichtig": "Važno", "schnell": "Brzo", "einfach": "Jednostavno", "klar": "Jasno",
    "vorteil": "Prednost", "nachteil": "Nedostatak", "loesen": "Rešiti", "planen": "Planirati",
    "notwendig": "Neophodno", "moeglich": "Moguće", "unmoeglich": "Nemoguće"
}

st.markdown("<h1 class='main-title'>LOGIC HACKER</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["DEKODIRAJ (DE)", "PREVEDI (SRB)"])

with tab1:
    search_de = st.text_input("Unesi nemačku reč:", placeholder="Kucaj ovde...", key="de")
    if search_de:
        st.write("---")
        results = []
        for de, srb in raw_data.items():
            if search_de.lower() in de.lower():
                results.append((de, srb))
        
        if results:
            for de_word, srb_word in results:
                st.markdown(f"""
                <div class='result-card'>
                    <h3 style='margin:0; color:#00f2fe;'>{de_word}</h3>
                    <p style='font-size:1.2rem; margin-top:5px; color:#E0E0E0;'>{srb_word}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info(f"Reč '{search_de}' nije pronađena u bazi.")

with tab2:
    search_srb = st.text_input("Unesi srpski pojam:", placeholder="Kucaj ovde...", key="srb")
    if search_srb:
        st.write("---")
        results_srb = []
        for de, srb in raw_data.items():
            if search_srb.lower() in srb.lower():
                results_srb.append((de, srb))
        
        if results_srb:
            for de_word, srb_word in results_srb:
                st.markdown(f"""
                <div class='result-card'>
                    <h3 style='margin:0; color:#00f2fe;'>{de_word}</h3>
                    <p style='font-size:1.1rem; margin-top:5px; color:#E0E0E0;'>Prevod za: {srb_word}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info(f"Pojam '{search_srb}' nije pronađen u bazi.")
