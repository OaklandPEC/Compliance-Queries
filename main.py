import requests
import json
import pandas as pd


#function that requests csv filename and API link
def getAPI():
    print("Hello! This program will output CSV files from Socrata,\n")
    print("at this point in time, please only use API from the API seciton of data.oaklandca.gov\n")
    csvName = input("What would you like to name this file?: ")
    print("               ")
    #stores API link as URL to feed to read_json
    api = input("Paste the link to the API here:  ")

    df = pd.read_json(api)
    df.head(5)
    print(df)
    #produces calculations based on data such as mean, min, percentage values and more.
    print(df.describe())
    #replace filepath as needed
    #potentially making edits to allow for this
    df.to_csv('/Users/chrismullins/dev/Public Ethics Comission/compliance queries/CSV/'+csvName+'.csv')

#Runs function
getAPI()




