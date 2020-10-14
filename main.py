import requests
import json
import csv
import pandas as pd
from csv import reader
from csv import writer

#function that requests API link
def getAPI():
    print("Hello! This program will output CSV files from Socrata,\n")
    print("at this point in time, please only use API from the API\n")
    print("section of data.oaklandca.gov")
    print("               ")
    api = input("Paste the link to the API here:  ")

    df = pd.read_json(api)
    df.head(5)
    print(df)
    print(df.describe())

#Currently only works for itemized cash contributions.
getAPI()




