import requests


response = requests.get(url='https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=boolean')
response.raise_for_status()
data = response.json()
question_data = data['results']