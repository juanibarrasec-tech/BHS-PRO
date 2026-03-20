import json
import os
import ollama

class AnalysisAgent:
    def __init__(self, model="llama3:8b"):
            self.log_path = "logs/recon_results.log"
                    self.bus_path = "data/json_bus/"
                            self.model = model

                                def read_last_recon(self):
                                        """Extrae los hallazgos del log de Nmap."""
                                                if os.path.exists(self.log_path):
                                                            with open(self.log_path, 'r') as f:
                                                                            data = f.read()
                                                                                            return data[-1500:] # Enviamos solo el final para no saturar la RAM
                                                                                                    return "Sin datos."

                                                                                                        def get_ai_advice(self, recon_data):
                                                                                                                """Consulta a Ollama localmente."""
                                                                                                                        print(f"[*] Analizando con {self.model}...")
                                                                                                                                try:
                                                                                                                                            response = ollama.chat(model=self.model, messages=[
                                                                                                                                                            {'role': 'system', 'content': 'Eres un experto en Bug Bounty. Analiza los puertos y servicios. Sugiere vectores de ataque como SQLi, XSS o IDOR basándote en los hallazgos. Sé breve y técnico.'},
                                                                                                                                                                            {'role': 'user', 'content': f"Resultados de Nmap:\n{recon_data}"}
                                                                                                                                                                                        ])
                                                                                                                                                                                                    return response['message']['content']
                                                                                                                                                                                                            except Exception as e:
                                                                                                                                                                                                                        return f"Error en IA Local: {e}"

                                                                                                                                                                                                                            def check_for_analysis_mission(self):
                                                                                                                                                                                                                                    mission_file = f"{self.bus_path}analysis_mission.json"
                                                                                                                                                                                                                                            if os.path.exists(mission_file):
                                                                                                                                                                                                                                                        with open(mission_file, 'r') as f:
                                                                                                                                                                                                                                                                        return json.load(f)
                                                                                                                                                                                                                                                                                return None
                                                                                                                                                                                                                                                                                
