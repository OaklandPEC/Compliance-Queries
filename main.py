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
    
    #Requests another API to append to the first one
    print('Would you like to add another API? Respond Y for Yes and N for No\n')
    userInput = input('Respond Y for Yes and N for No\n')
    if userInput == 'Y':
        api2 = input('Paste the link to the API here')
        df2 = pd.read_json(api2)
        df.append(df2)
        df.to_csv('/Users/chrismullins/dev/Public Ethics Comission/compliance queries/CSV/'+csvName+'.csv')
        print('File created!\n')
        print(df.describe())
    elif userInput == 'N':
        print('We will not add another API at this time.')
    else:
        print('Sorry, please response with either Y or N')
    #Data visualization

#Runs function

getAPI()



