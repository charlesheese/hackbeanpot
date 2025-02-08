import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY  # Load API key from .env

async def analyze_carbon_footprint(data: dict):
    """
    Sends user's carbon footprint data to OpenAI and returns analysis.
    """
    prompt = f"""
    The user provided the following carbon footprint data:
    - Transportation: {data["transportation"]}
    - Diet: {data["diet"]}
    - Electricity Usage: {data["electricity_usage"]}
    - Other Factors: {data["other_factors"]}
    
    1. Estimate the user's carbon footprint in kg CO2e.
    2. Suggest two personalized recommendations to reduce their footprint.
    
    Return the response in this format:
    - Carbon Score: (numeric value)
    - Recommendations: (list of two short suggestions)
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["choices"][0]["message"]["content"]
    
    # Extract data from OpenAI response
    lines = result.split("\n")
    carbon_score = float(lines[0].split(":")[1].strip())  # Extract numeric score
    recommendations = [line.strip() for line in lines[1:] if line]

    return carbon_score, recommendations
