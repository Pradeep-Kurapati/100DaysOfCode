from datetime import datetime

import requests
import time

# Constants
MY_LAT = 17.361719
MY_LONG = 78.475166

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG
}

response = requests.get(url='https://api.sunrise-sunset.org/json?formatted=0', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
