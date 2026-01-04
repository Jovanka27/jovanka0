import streamlit as st

# Postavke ekrana
st.set_page_config(page_title="German Logic Hacker", layout="wide")

# Dark Terminal Look
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #00ff41; font-family: monospace; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00ff41; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 GERMAN LOGIC HACKER")
st.write("Sistem: Prompt-based Decoding Engine")

# --- PROMPT SEKCIJA (Ono što si tražila) ---
logic_prompt = """
CILJ: Dešifruj nemačku reč/rečenicu.
OPERATIVNI SISTEM: Engleski jezik.
METOD: Reverse Engineering.
1. Razbij složenicu na logičke delove.
2. Objasni prefikse kao funkcije.
3. Daj primer za Team Leadere (Executive Level).
"""

# Input polje
user_input = st.text_input("Unesi nemački 'kod' (reč ili frazu):", placeholder="npr. Entscheidungsspielraum")

if user_input:
    st.divider()
    st.subheader("Analiza:")
    # Ovde simuliramo rad prompta na bazi tvojih pravila
    if "Entscheidung" in user_input:
        st.code(f"PROMPT LOGIC: {logic_prompt}")
        st.success("DECODED: Ent- (removal) + Scheidung (separation) = Decision. Spielraum = Room to play/scope.")
        st.info("EXECUTIVE USAGE: 'Wir brauchen mehr Entscheidungsspielraum u ovom projektu.'")
    else:
        st.warning("Sistem spreman. Za punu AI integraciju potreban je API ključ, ali tvoja logika prompta je učitana!")

st.caption("v1.2 | Mode: GitHub Prompt Integration")
