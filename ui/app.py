import streamlit as st
import os
from core.reporter_agent import ReporterAgent

# Configuración de la página (Modo Oscuro forzado)
st.set_page_config(page_title="BHS-PRO Control", page_icon="😈", layout="centered")

st.title("😈 BHS-PRO: Squad Control")
st.markdown("---")

target = st.text_input("🎯 Objetivo (IP o Dominio):", placeholder="ejemplo.com")
task = st.selectbox("🛠️ Misión:", ["Reconocimiento (Nmap)", "Escaneo de Vulnerabilidades", "Análisis IA"])

if st.button("🚀 Lanzar Squad"):
    if target:
        reporter = ReporterAgent()
        mission = reporter.create_mission("recon", target, task)
        st.success(f"✅ Misión enviada al Bus: {target}")
        st.info("Revisa la terminal del Orquestador para ver el progreso.")
    else:
        st.error("⚠️ Por favor, ingresa un objetivo.")

st.sidebar.markdown("### 📊 Estado de la Squad")
st.sidebar.write("Orquestador: 🟢 Online")
st.sidebar.write("Agente Recon: 🟢 Listo")

