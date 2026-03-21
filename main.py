import os
import time
import json
from core.recon_agent import ReconAgent
from core.reporter_agent import ReporterAgent
from core.analysis_agent import AnalysisAgent
from core.final_report_agent import FinalReportAgent
from core.comm_agent import CommAgent

def main():
    print("🛡️ BHS-PRO: Orquestador Multi-Agente Iniciado")
    print("[*] Vigilando el Bus de Datos... (Presiona Ctrl+C para salir)")
    
    # Inicializar agentes
    recon = ReconAgent()
    reporter = ReporterAgent()
    analyzer = AnalysisAgent(model="llama3:8b") # Asegúrate que este sea tu modelo de Ollama
    final_report = FinalReportAgent()
    notifier = CommAgent()

    bus_path = "data/json_bus/"

    while True:
        # 1. Buscar misiones de Reconocimiento
        if os.path.exists(f"{bus_path}recon_mission.json"):
            with open(f"{bus_path}recon_mission.json", "r") as f:
                mission = json.load(f)
            
            target = mission['target']
            print(f"\n[!] Nueva Misión Detectada: Recon sobre {target}")
            
            # Ejecutar Nmap
            recon_results = recon.run_nmap_scan(target)
            print(f"[✔] Reconocimiento completado.")
            
            # Borrar misión procesada
            os.remove(f"{bus_path}recon_mission.json")

        # 2. Buscar misiones de Análisis IA
        if os.path.exists(f"{bus_path}analysis_mission.json"):
            print("[!] Iniciando Fase de Inteligencia con Ollama...")
            
            # Leer datos de Nmap y pedir consejo a la IA
            raw_data = analyzer.read_last_recon()
            advice = analyzer.get_ai_advice(raw_data)
            
            print(f"\n[IA]: {advice[:200]}...") # Mostrar resumen en terminal

            # 3. Generar Reporte Profesional (.md)
            report_path = final_report.generate_markdown(target, advice)
            print(f"[✔] Reporte guardado en: {report_path}")

            # 4. Alerta Crítica (Discord/Ntfy)
            keywords = ["CRÍTICO", "VULNERABILIDAD", "EXPLOTABLE", "RCE", "SQL", "XSS"]
            if any(k in advice.upper() for k in keywords):
                notifier.send_alert(target, advice)

            # Borrar misión procesada
            os.remove(f"{bus_path}analysis_mission.json")

        time.sleep(2) # Evitar saturar el CPU de tu móvil

if __name__ == "__main__":
    main()
