import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = pickle.load(open('app/model.pickle', 'rb'))

app = FastAPI()

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
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    
    return {"Attrition": "Yes" if prediction[0] == 1 else "No"}

