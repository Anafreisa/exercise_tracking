import requests
import os
from datetime import datetime

APP_ID = "5b31d342"
API_KEY = "2ff47bf64cbe88bd8ea4e6ebe3f14d91"
TOKEN = "ksmdfkmksmdfkmsdfksdkfmskksd"

GENDER = "female"
WEIGHT_KG = 102
HEIGHT_CM = 165
AGE = 35

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/b1a2a30c681f6bc9e4dce1303cb84447/workoutTracking/workouts"

today = datetime.now().strftime("%d/%m/%Y")
hour = datetime.now().strftime("%X")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheety_inputs = None
for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today,
            "time": hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheety_inputs, headers=sheety_headers)
    print(sheet_response.text)
