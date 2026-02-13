import joblib
import os
from config import MODEL_PATH

class ModelAgent:

    def __init__(self):
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
        else:
            self.model = None

    def predict(self, df):
        if self.model:
            df["ml_score"] = self.model.predict_proba(
                df[["rating", "form_score", "weight_factor", "draw_bias"]]
            )[:, 1]
        else:
            df["ml_score"] = df["total_score"] / df["total_score"].max()

        return df
