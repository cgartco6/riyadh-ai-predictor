from agents.orchestrator import StrategicOrchestrator
from config import RACE_URLS
import json

if __name__ == "__main__":
    orchestrator = StrategicOrchestrator()

    for url in RACE_URLS:
        result = orchestrator.execute(url)
        print(result)

        result.to_json("output/predictions.json", orient="records")
