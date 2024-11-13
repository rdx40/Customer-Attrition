# main.py
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load the pickled model
model = pickle.load(open('app/model.pickle', 'rb'))

# Initialize FastAPI app
app = FastAPI()

# Define the input data structure
class EmployeeData(BaseModel):
    Age: int
    NumCompaniesWorked: int
    JobSatisfaction: int
    PerformanceRating: int
    MonthlyIncome: float
    JobLevel: int
    DistanceFromHome: int

@app.post("/predict")
def predict(data: EmployeeData):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Perform normalization if needed (using the same scaler as before)
    # If you saved a scaler, load it similarly to the model
    # scaler = pickle.load(open('scaler.pkl', 'rb'))
    # input_data_scaled = scaler.transform(input_data)
    
    # Predict using the loaded model
    prediction = model.predict(input_data)
    
    return {"Attrition": "Yes" if prediction[0] == 1 else "No"}

# To run the FastAPI app, use the command: uvicorn main:app --reload

