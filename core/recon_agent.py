import json
import subprocess
import os
from datetime import datetime

class ReconAgent:
    def __init__(self):
        self.bus_path = "data/json_bus/"
        self.results_path = "logs/recon_results.log"

    def read_mission(self):
        """Busca misiones pendientes en el JSON Bus."""
        mission_file = f"{self.bus_path}recon_mission.json"
        if os.path.exists(mission_file):
            with open(mission_file, 'r') as f:
                return json.load(f)
        return None

    def run_nmap_scan(self, target):
        """Ejecuta un escaneo rápido usando los binarios de Termux."""
        print(f"[*] Iniciando Recon en: {target}")
        try:
            # Escaneo básico de puertos comunes (Modo sigilo -sS si tienes root)
            command = f"nmap -F {target}"
            result = subprocess.check_output(command, shell=True).decode()
            
            self._save_log(target, result)
            return result
        except Exception as e:
            return f"Error en Recon: {e}"

    def _save_log(self, target, data):
        with open(self.results_path, "a") as f:
            f.write(f"\n--- RECON: {target} [{datetime.now()}] ---\n{data}\n")

if __name__ == "__main__":
    recon = ReconAgent()
    mission = recon.read_mission()
    if mission:
        print(f"Misión recibida para: {mission['target']}")
        recon.run_nmap_scan(mission['target'])
from core.scope_validator import is_in_scope

def run_nmap_scan(self, target):
    if not is_in_scope(target):
        print(f"⚠️ BLOQUEADO: {target} está fuera de Scope!")
        return "Fuera de alcance"  # <--- Esta línea debe estar alineada aquí

                            
