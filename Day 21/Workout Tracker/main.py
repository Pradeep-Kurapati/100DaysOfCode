import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
TOKEN = os.environ['TOKEN']
API_KEY = os.environ['API_KEY']
SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']

tracking_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

activity = input('What did you do today? ')

parameters = {
    'query': activity
}

HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

response = requests.post(url=tracking_url, json=parameters, headers=HEADERS)
data = response.json()
print(data)

# exercise = data['exercises'][0]['user_input']
# calories = data['exercises'][0]['nf_calories']
# duration = data['exercises'][0]['duration_min']

date = datetime.now()
date = date.strftime('%d%m%Y')

exercise_time = datetime.now()
exercise_time = exercise_time.strftime("%H:%M:%S")

sheet_inputs = {
    "workout": {
        "date": date,
        "time": exercise_time,
        "exercise": data['exercises'][0]["name"].title(),
        "duration": data['exercises'][0]["duration_min"],
        "calories": data['exercises'][0]["nf_calories"]
    }
}

auth_parameters = {
    'Authorization': TOKEN
}

response2 = requests.post(url='https://api.sheety.co/39ce532d89d47f91a94b03bbb55f46ae/workout/workouts',
                          json=sheet_inputs, headers=auth_parameters)

print(response2.text)
