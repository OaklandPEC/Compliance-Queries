import requests
import json

scheduleA_api = 'https://data.oaklandca.gov/resource/3xq4-ermg.json'

response = requests.get(scheduleA_api)

scheduleA_dict = response.json()

for item in scheduleA_dict:
    print(item['filer_id'])


