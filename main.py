import requests
import json
import csv
import pandas as pd
from csv import reader
from csv import writer


df = pd.read_json('https://data.oaklandca.gov/resource/3xq4-ermg.json')
df.head(5)

print(df)
