from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


app = FastAPI(title="Health Risk Classifier API")

# SAFE MODEL LOADING (prevents crash if model issues exist)
try:
    model = joblib.load("model.pkl")
    model_loaded = True
except Exception as e:
    model_loaded = False
    model = None
    print("Model loading error:", e)


# Root endpoint (this MUST always work)
@app.get("/")
def home():
    return {
        "message": "API is running successfully",
        "model_loaded": model_loaded
    }


# Input schema (MUST match your training columns order)
class HealthInput(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree: float
    age: float


# Prediction endpoint
@app.post("/predict")
def predict(data: HealthInput):
    try:
        import pandas as pd

        features = pd.DataFrame([{
            "pregnancies": data.pregnancies,
            "glucose": data.glucose,
            "blood_pressure": data.blood_pressure,
            "skin_thickness": data.skin_thickness,
            "insulin": data.insulin,
            "bmi": data.bmi,
            "diabetes_pedigree": data.diabetes_pedigree,
            "age": data.age
        }])

        prediction = model.predict(features)[0]

        try:
            probability = model.predict_proba(features)[0][1]
        except:
            probability = None

        return {
            "prediction": int(prediction),
            "probability": float(probability) if probability else "N/A"
        }

    except Exception as e:
        return {"error": str(e)}