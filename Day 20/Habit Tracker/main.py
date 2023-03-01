import requests
from datetime import datetime

USER_NAME = 'kpradeep7'
TOKEN = 'pradeep@123'
GRAPH_ID = 'graph1'

API_ENDPOINT = 'https://pixe.la/v1/users'
parameters = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# Creating User
# response = requests.post(url=API_ENDPOINT, json=parameters)
# print(response.text)

HEADERS = {
        'X-USER-TOKEN': TOKEN
}

graph_parameters = {
    'id': GRAPH_ID,
    'name': 'Gym',
    'unit': 'Km',
    'type': 'float',
    'color': 'shibafu'

}
# Creating graph
# GRAPH_API = f'{API_ENDPOINT}/{USER_NAME}/graphs'
# response = requests.post(url=GRAPH_API, headers=HEADERS, json=graph_parameters)
# print(response.text)

# Posting a pixel
PIXEL_API = f'{API_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}'

today = datetime(day=28, month=2, year=2023)
today = today.strftime('%Y%m%d')
POSTING_PARAMETERS = {
    # 'id': GRAPH_ID,
    # 'name': 'Gym',
    # 'unit': 'Km',
    # 'type': 'float',
    # 'color': 'shibafu',
    'date': today,
    'quantity': '2'
}
# response = requests.post(url=PIXEL_API, json=POSTING_PARAMETERS, headers=HEADERS)
# print(response.text)

UPDATE_ENDPOINT = f'{API_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today}'
UPDATE_PARAMETERS = {
    'quantity': '10'
}
# response = requests.put(url=UPDATE_ENDPOINT, json=UPDATE_PARAMETERS, headers=HEADERS)
# print(response.text)

response = requests.delete(url=UPDATE_ENDPOINT, headers=HEADERS)
print(response.text)