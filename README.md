# 🩺 Health Risk Predictor

This project predicts whether a patient is at risk of diabetes using a machine learning model.

## Features
- FastAPI backend for predictions
- Streamlit frontend for user interaction
- Trained ML model using Pima Indians dataset

## How to Run Locally

### 1. Start API
uvicorn main:app --reload

### 2. Start Frontend
streamlit run app.py

## Input Features
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree
- Age

## Output
- Prediction (0 = Low Risk, 1 = High Risk)
- Probability score
