import time
import os
from core.recon_agent import ReconAgent
from core.reporter_agent import ReporterAgent

def main():
    print("🛡️  BHS-PRO: Orquestador Multi-Agente Iniciado")
    print("[*] Monitoreando JSON Bus para nuevas misiones...")
    
    recon = ReconAgent()
    reporter = ReporterAgent()

    while True:
        # 1. El Agente de Recon revisa si hay misiones de escaneo
        mission = recon.read_mission()
        
        if mission:
            target = mission.get('target')
            print(f"\n[!] Misión Detectada: Escaneando {target}")
            
            # Ejecutar el escaneo
            result = recon.run_nmap_scan(target)
            
            # 2. El Agente de Reporte procesa el resultado y limpia el Bus
            print(f"[+] Recon completado para {target}. Generando log...")
            
            # Borrar la misión para que no se repita en el siguiente ciclo
            mission_file = "data/json_bus/recon_mission.json"
            if os.path.exists(mission_file):
                os.remove(mission_file)
                print(f"[*] Bus Limpio. Esperando nueva misión...")
        
        # Pausa para no saturar el CPU de Termux
        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Orquestador detenido por el usuario.")
