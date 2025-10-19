import pandas as pd
import joblib

def load_model():
    model = joblib.load("model.pkl")
    return model

def predict_restock(month, festival, sales):
    model = load_model()
    month_code = month - 1  # assuming month 1–12
    fest_flag = 1 if festival == "Yes" else 0
    data = pd.DataFrame([[month_code, fest_flag, sales]], columns=['Month', 'Festival', 'Sales'])
    prediction = model.predict(data)[0]
    return round(prediction, 2)
