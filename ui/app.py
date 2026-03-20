import streamlit as st

st.set_page_config(page_title="BHS-PRO", layout="wide")

# Estilo Oscuro Forzado
st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: #00ff41; }
            input { background-color: #161b22 !important; color: #00ff41 !important; }
                </style>
                    """, unsafe_allow_html=True)

                    st.title("🛡️ BugHunter Squad PRO")
                    target = st.text_input("Objetivo:", "example.com")
                    if st.button("Lanzar Squad"):
                        st.write(f"Iniciando misión para {target}...")
                        
