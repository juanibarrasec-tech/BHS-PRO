import json
import os
from datetime import datetime

class ReporterAgent:
  def __init__(self):
            self.bus_path = "data/json_bus/"
                    os.makedirs(self.bus_path, exist_ok=True)

   def create_mission(self, agent_name, target, task):
                                mission = {
                                            "id": datetime.now().strftime("%Y%m%d%H%M"),
                                                        "target": target,
                                                                    "task": task,
                                                                                "status": "active"
                                                                                        }
                                                                                                with open(f"{self.bus_path}{agent_name}_mission.json", "w") as f:
                                                                                                            json.dump(mission, f, indent=4)
                                                                                                                    return mission
                                                                                                                    
