import requests

class CommAgent:
    def __init__(self):
      # Elige un nombre de canal único que nadie más use
        self.topic = "bhs_pro_alertas_DevSkull_666" 
        self.enabled = True

    def send_alert(self, target, analysis):
        if not self.enabled: return
        
        print(f"[*] Enviando alerta a Ntfy: {self.topic}")
        try:
            requests.post(f"https://ntfy.sh/{self.topic}",
                data=f"⚠️ Hallazgo Crítico en {target}!\nVerifica el reporte en Termux.",
                headers={
                    "Title": "BHS-PRO SQUAD ALERT",
                    "Priority": "high",
                    "Tags": "skull,warning"
                })
            print("[✔] Notificación enviada al móvil.")
        except Exception as e:
            print(f"[X] Error de notificación: {e}")
