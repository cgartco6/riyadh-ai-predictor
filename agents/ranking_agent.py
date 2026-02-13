class RankingAgent:

    def rank(self, df):
        df = df.sort_values("simulated_win_prob", ascending=False)
        return df[["name", "simulated_win_prob"]]
