from typing import Dict, Any 
import math 
import pandas as pd 


car_emissions_csv = "backend\app\services\CO2 Emissions_Canada.csv.numbers"

def load_car_emissions():
    try:
        df = pd.read_csv(car_emissions_csv)
        return df
    except Exception as e:
        return {"error": str(e)}
    
def find_car_emission(make:str, model: str):
    df = load_car_emissions()

    if isinstance(df, dict):
        return df

    car = df[(df[""])]

