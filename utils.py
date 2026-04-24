import requests

API_URL = "https://health-risk-predictor-3wvi.onrender.com"

# 🔮 Prediction function
def predict_health(data):
    try:
        response = requests.post(f"{API_URL}/predict", json=data, timeout=5)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "API returned an error"}

    except requests.exceptions.RequestException:
        return {"error": "API connection failed"}


# ❤️ Health check
def check_api():
    try:
        res = requests.get(f"{API_URL}/health", timeout=3)
        return res.status_code == 200
    except:
        return False