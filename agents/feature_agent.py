class FeatureAgent:

    def build(self, df):
        df["weight_factor"] = 65 - df["weight"]
        df["draw_bias"] = 10 - df["draw"]
        df["total_score"] = (
            df["rating"] * 0.5 +
            df["form_score"] * 0.3 +
            df["weight_factor"] * 0.1 +
            df["draw_bias"] * 0.1
        )
        return df
