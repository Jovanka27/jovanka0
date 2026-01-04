
import streamlit as st

st.set_page_config(page_title="Logic Hacker", layout="wide")

# Hacker Style CSS
st.markdown("""<style>.main { background-color: #0d0d0d; color: #00ff41; font-family: monospace; }</style>""", unsafe_allow_html=True)

st.title("📟 GERMAN LOGIC HACKER")

# Baza znanja - Logika
prefixes = {
    "ver-": "CHANGE/ERROR (Kompletna promena stanja)",
    "be-": "PROCESS (Pravi glagol aktivnim prema objektu)",
    "ent-": "DE- / REMOVAL (Oduzimanje ili rešenje)",
    "ab-": "OFF / AWAY (Odvajanje)"
}

compounds = {
    "arbeit": "Work", "vertrag": "Contract", "kündigung": "Termination",
    "frist": "Deadline", "versicherung": "Insurance", "plan": "Schedule"
}

# Input polje
word = st.text_input("Unesi nemačku reč za dešifrovanje:").lower()

if word:
    st.subheader("Analiza koda:")
    # Provera prefiksa
    for p, desc in prefixes.items():
        if word.startswith(p.replace("-", "")):
            st.warning(f"OPERATOR: {p} -> {desc}")
    
    # Provera delova reči
    for part, eng in compounds.items():
        if part in word:
            st.success(f"DEO: {part} -> {eng}")
    
    if "arbeit" in word and "vertrag" in word:
        st.info("LOGIKA: Work + Contract = Employment Agreement")
else:
    st.write("Sistem spreman. Unesi npr. 'Arbeitsvertrag'")
