import streamlit as st
from openai import OpenAI

# --- ULTRACLEAN CONFIG ---
st.set_page_config(page_title="Logic Hacker", page_icon="📟", layout="wide")

# --- CYBER UI STYLE ---
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00ff41; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #111; color: #00ff41; border: 1px solid #00ff41; border-radius: 5px; }
    .stSelectbox>div>div>div { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #00ff41; }
    .stTextArea>div>div>textarea { background-color: #111; color: #00ff41; border: 1px solid #00ff41; }
    p, label { color: #00ff41 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: KONTROLNI CENTAR ---
with st.sidebar:
    st.title("📟 SYSTEM CORE")
    st.write("---")
    key_input = st.text_input("UNESI API KLJUČ:", type="password", help="Ovde nalepi sk-... ključ sa OpenAI sajta")
    
    st.write("### MOD RADA")
    mode = st.radio("", 
        ["DEŠIFROVANJE (DE -> SRB)", "PREVOD (SRB/EN -> DE)"])
    
    st.divider()
    st.caption("LOGIC HACKER v5.5 // ONLINE")

# --- GLAVNI TERMINAL ---
st.title("LOGIC HACKER TERMINAL")

if not key_input:
    st.error("🔑 SISTEM ZAKLJUČAN: Unesi API ključ u bočnom meniju da aktiviraš globalnu bazu.")
    st.info("Kada uneseš ključ, aplikacija će moći da dešifruje BILO KOJU nemačku reč ili rečenicu.")
else:
    # Inicijalizacija klijenta sa tvojim ključem
    client = OpenAI(api_key=key_input)
    
    label_text = "UNESI NEMAČKI KOD ZA ANALIZU:" if mode == "DEŠIFROVANJE (DE -> SRB)" else "UNESI SRPSKU/ENGLESKU FRAZU:"
    user_query = st.text_area(label_text, height=100, placeholder="Piši ovde...")

    if st.button("EXECUTE"):
        if user_query:
            st.write("---")
            with st.spinner("SCANNING GLOBAL DATABASE..."):
                try:
                    if mode == "DEŠIFROVANJE (DE -> SRB)":
                        prompt = f"""
                        Analiziraj nemački tekst: '{user_query}'.
                        1. Daj direktan prevod na srpski.
                        2. Ako je reč složenica, rastavi je na delove i objasni logiku prefiksa.
                        Odgovaraj u hakerskom stilu, kratko i pregledno.
                        """
                    else:
                        prompt = f"""
                        Prevedi '{user_query}' na nemački jezik.
                        Daj mi:
                        - Formalnu verziju (za ugovore/šefove)
                        - Direktnu verziju (za kolege)
                        - Logičko objašnjenje ključne reči u prevodu.
                        """

                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "Ti si vrhunski lingvistički haker. Dešifruješ nemački jezik na srpski precizno i logično."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    
                    st.subheader("🔓 REZULTAT:")
                    st.code(response.choices[0].message.content, language="markdown")
                
                except Exception as e:
                    st.error(f"GREŠKA U VEZI: Proveri da li je API ključ ispravan ili imaš li kredita na OpenAI nalogu.")
        else:
            st.warning("Unesi tekst za obradu.")

# --- FOOTER ---
st.write("---")
st.caption("UNLIMITED DATA ACCESS // ENCRYPTION: ACTIVE")
