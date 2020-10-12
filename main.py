import requests

scheduleA_api = 'https://data.oaklandca.gov/resource/3xq4-ermg.json'

response = requests.get(scheduleA_api)

print(response.text)