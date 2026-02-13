import pandas as pd

class NormalizationAgent:

    def process(self, raw_data):
        df = pd.DataFrame(raw_data)

        df["form_score"] = df["form"].apply(self.convert_form)

        return df

    def convert_form(self, form):
        score = 0
        for c in form:
            if c.isdigit():
                score += (10 - int(c))
        return score
