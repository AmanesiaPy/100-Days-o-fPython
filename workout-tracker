import requests
from  datetime import datetime

website_url = "https://trackapi.nutritionix.com"

API_ID = "151a87f7"
API_KEY = "1b36207264eded4409464d77ca556b71"

exercise_endpoint = f"{website_url}/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
exercises = response.json()["exercises"]
# print(exercises)

sheety_url = "https://api.sheety.co/579b1210e30d7e4d087584521d7788f4/exerciseTracker/workouts"

now = datetime.now()
date = now.date()
time = now.time()

token = {
    "Authorization": "Bearer sdioajdioaewjdjawdajeij",
}
for exercise in exercises:
    sheety_parameters = {
        "workout": {
            "date": date.strftime('%d/%m/%Y'),
            "time": time.strftime('%X'),
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"]),
        }
    }
    # print(sheety_parameters)

    update_row = requests.post(url=sheety_url, json=sheety_parameters, headers=token)
    print(update_row.text)
