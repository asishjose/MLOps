import joblib
import os

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
        _model = joblib.load(model_path)
    return _model