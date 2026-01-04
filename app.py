import streamlit as st

st.set_page_config(page_title="Logic Hacker Enterprise", layout="wide")

# Dark Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #00ff41; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00ff41; border: 1px solid #00ff41; }
    .stHeader { border-bottom: 2px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 GERMAN LOGIC HACKER - ENTERPRISE BAZA")

# --- VELIKA LOGIČKA BAZA ---
# Prefiksi (Operatori radnje)
prefixes = {
    "ver-": "PROMENA/GREŠKA: Menja status (npr. verhandeln - pregovarati, verwalten - upravljati)",
    "be-": "AKTIVACIJA: Usmerava radnju na direktan objekat (npr. bestätigen - potvrditi)",
    "ent-": "DE-KONSTRUKCIJA: Uklanjanje ili konačna odluka (npr. entlassen - otpustiti)",
    "ab-": "ODVAJANJE/ZAVRŠETAK: (npr. abrechnung - obračun, abgabetermin - rok predaje)",
    "an-": "POKRETANJE: (npr. antrag - zahtev, anweisung - instrukcija)",
    "auf-": "PODIZANJE/OTVARANJE: (npr. aufgabe - zadatak, aufwand - trošak/napor)",
    "aus-": "OUT/IZLAZ: (npr. auszahlung - isplata, ausbildung - obuka)",
    "mit-": "SU- / KO-: Saradnja (npr. mitwirkung - sudelovanje)",
    "vor-": "PRE-/ISPRED: (npr. vorstand - uprava, vorbereitung - priprema)",
    "zu-": "KA/DODATAK: (npr. zustimmung - saglasnost, zuschlag - doplata)"
}

# Koreni reči (Data Entities)
logic_map = {
    # MENADŽMENT & HR
    "leitung": "Rukovođenje / Uprava",
    "personal": "Ljudski resursi / Osoblje",
    "vertrag": "Ugovor",
    "kündigung": "Otkaz / Raskid",
    "einstellung": "Zapošljavanje / Postavka",
    "führung": "Vođenje / Liderstvo",
    "gespräch": "Razgovor / Sastanak",
    # FINANSIJE & ADMIN
    "rechnung": "Račun / Obračun",
    "gehalt": "Plata",
    "steuer": "Porez",
    "versicherung": "Osiguranje",
    "aufwand": "Napor / Trošak",
    "ertrag": "Prinos / Profit",
    # PROCESI
    "entscheidung": "Odluka",
    "frist": "Rok",
    "termin": "Zakazan termin",
    "vereinbarung": "Sporazum / Dogovor",
    "optimierung": "Optimizacija",
    "planung": "Planiranje",
    "bericht": "Izveštaj",
    "anforderung": "Zahtev / Requirement",
    "umsetzung": "Implementacija / Primena"
}

# --- INTERFEJS ---
word = st.text_input("UNESI POJAM (npr. Gehaltsabrechnung, Projektleitung, Versicherungsvertrag):").lower()

if word:
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚙️ Logički Operatori")
        found_pre = False
        for p, desc in prefixes.items():
            if word.startswith(p.replace("-", "")):
                st.info(f"**{p}**\n{desc}")
                found_pre = True
        if not found_pre: st.write("Nema detektovanih standardnih prefiksa.")

    with col2:
        st.subheader("🔓 Dekodirani Elementi")
        found_map = False
        for part, srb in logic_map.items():
            if part in word:
                st.success(f"**{part.upper()}**\n{srb}")
                found_map = True
        if not found_map: st.write("Nema prepoznatih elemenata u bazi.")
    
    # Reverse Engineering Logic (Primeri kombinacija)
    if found_pre and found_map:
        st.divider()
        st.write("💡 **HACKER INSIGHT:** Ova reč je složenica. Tvoj mozak treba da je čita s desna na levo za bukvalno značenje, a prefiks definiše 'mod' radnje.")
else:
    st.info("Sistem spreman. Baza sadrži ključne termine za Team Leadere.")

# --- DODATNA STATISTIKA ---
with st.expander("📊 Pogledaj celu bazu prefiksa"):
    for k, v in prefixes.items():
        st.write(f"**{k}** : {v}")

