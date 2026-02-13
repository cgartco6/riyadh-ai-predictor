import numpy as np

class SimulationAgent:

    def run(self, df, predictions, simulations=10000):
        win_counts = {name: 0 for name in df["name"]}

        probabilities = df["ml_score"].values
        probabilities /= probabilities.sum()

        for _ in range(simulations):
            winner = np.random.choice(df["name"], p=probabilities)
            win_counts[winner] += 1

        df["simulated_win_prob"] = df["name"].map(
            lambda x: win_counts[x] / simulations
        )

        return df
