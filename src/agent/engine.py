import numpy as np
from pathlib import Path

# Optional imports for model loading (only if model exists)
try:
    import joblib
    HAS_JOBLIB = True
except ImportError:
    HAS_JOBLIB = False

MODEL_PATH = Path(__file__).parent.parent / "models" / "psa_model_v1.pkl"

class PricingAgent:
    def __init__(self, model_path=MODEL_PATH):
        # Lazy load model; in production use startup event
        self.model = None
        if model_path.exists() and HAS_JOBLIB:
            try:
                self.model = joblib.load(model_path)
            except Exception:
                # If model loading fails (e.g., missing scikit-learn), use fallback
                self.model = None

    def _predict_units(self, features):
        if self.model is None:
            # fallback simple heuristic if no model
            return max(1, int(100 * np.random.rand()))
        try:
            return int(self.model.predict([features])[0])
        except Exception:
            # If prediction fails (e.g., missing scikit-learn), use fallback
            return max(1, int(100 * np.random.rand()))

    def recommend_price(self, product_id, cost_price, competitor_price=None, demand_level=None, min_margin=0.1, max_price=None):
        # Build candidate prices (simple grid around competitor/cost)
        candidates = [round(cost_price * (1 + r/100), 2) for r in range(10, 101, 5)]
        best = {"price": cost_price, "profit": -1, "units": 0}
        for p in candidates:
            # build feature vector for model: (price, cost, competitor_price, demand_level_encoded)
            features = [p, cost_price, competitor_price if competitor_price else 0, 1 if demand_level=='High' else 0]
            predicted_units = self._predict_units(features)
            profit = (p - cost_price) * predicted_units
            if profit > best["profit"] and (max_price is None or p <= max_price) and (p - cost_price)/p >= min_margin:
                best = {"price": p, "profit": profit, "units": predicted_units}
        return {
            "recommended_price": best["price"],
            "predicted_units": best["units"],
            "predicted_profit": best["profit"],
            "status": "SUCCESS"
        }
