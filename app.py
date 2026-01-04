import streamlit as st

st.set_page_config(page_title="Logic Hacker", layout="wide")

# Hacker Style UI
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #00ff41; font-family: monospace; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00ff41; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 GERMAN LOGIC HACKER")

# BAZA LOGIKE
logic_map = {
    "arbeit": "WORK / LABOR",
    "vertrag": "CONTRACT / AGREEMENT",
    "kündigung": "TERMINATION / RESIGNATION",
    "frist": "DEADLINE / PERIOD",
    "versicherung": "INSURANCE",
    "plan": "SCHEDULE / PLAN"
}

prefixes = {
    "ver-": "LOGIC: Change of state / Modification",
    "be-": "LOGIC: Process / Action directed at object",
    "ent-": "LOGIC: Removal / Reversal"
}

# INPUT
word = st.text_input("Unesi nemačku reč za dešifrovanje:").lower()

if word:
    st.divider()
    st.subheader("Analiza sistema:")
    
    found = False
    # Provera prefiksa
    for p, desc in prefixes.items():
        if word.startswith(p.replace("-", "")):
            st.warning(f"⚙️ OPERATOR DETEKTOVAN: {p}")
            st.write(desc)
            found = True
            
    # Provera korena reči
    for part, translation in logic_map.items():
        if part in word:
            st.success(f"🔓 DEŠIFROVAN DEO: {part.upper()} -> {translation}")
            found = True
            
    if not found:
        st.error("Reč nije u bazi. Probaj: Arbeitsvertrag ili Kündigungsfrist.")
else:
    st.info("Sistem spreman. Unesi reč iz ugovora ili maila.")

