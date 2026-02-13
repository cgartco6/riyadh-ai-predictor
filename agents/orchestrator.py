from agents.scraper_agent import ScraperAgent
from agents.normalization_agent import NormalizationAgent
from agents.feature_agent import FeatureAgent
from agents.model_agent import ModelAgent
from agents.simulation_agent import SimulationAgent
from agents.ranking_agent import RankingAgent

class StrategicOrchestrator:

    def __init__(self):
        self.scraper = ScraperAgent()
        self.normalizer = NormalizationAgent()
        self.feature = FeatureAgent()
        self.model = ModelAgent()
        self.sim = SimulationAgent()
        self.rank = RankingAgent()

    def execute(self, race_url):
        raw = self.scraper.scrape(race_url)
        normalized = self.normalizer.process(raw)
        features = self.feature.build(normalized)
        predictions = self.model.predict(features)
        simulated = self.sim.run(features, predictions)
        final = self.rank.rank(simulated)

        return final
