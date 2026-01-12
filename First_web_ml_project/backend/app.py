from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# Enable CORS (important for frontend-backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = pickle.load(open("New_toUse_model.pkl", "rb"))

# Input schema
class InputData(BaseModel):
    combined: float

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Prepare input in same format as training
    df = pd.DataFrame([[data.combined]], columns=["combined"])

    prediction = model.predict(df)[0]

    return {
        "prediction": int(prediction),
        "result": "Benign" if prediction == 1 else "Malignant"
    }
