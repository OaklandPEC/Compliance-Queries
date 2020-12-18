import requests
import json
import pandas as pd
from datetime import datetime
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.oaklandca.gov", None)

#Dictionary containing all data
#Itemized is Schedule A and Non-Monetary Contributions is Schedule C
dataDict =  {'Summary Totals': "rsxe-vvuw", 'Late Contributions': "qact-u8hq", 'Non-Monetary Contributions': "ba44-jqtm", 'Itemized Cash Contributions': "3xq4-ermg"}
#TODO: Integrate some kind of select screen where you can highlight the different types of documents to use their dictionary value

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.oaklandca.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results1 = client.get(dataDict['Itemized Cash Contributions'], limit=100000)
results2 = client.get(dataDict['Non-Monetary Contributions'], limit=100000)

# Convert to pandas DataFrame
results_df1 = pd.DataFrame.from_records(results1)
results_df2 = pd.DataFrame.from_records(results2)

#Append Schedule C filer_id to Schedule A
results_df1.append(results_df2['filer_id'])
results_df1['tran_date'] = pd.to_datetime(results_df1['tran_date'])
results_df1.sort_values(by='tran_date', axis='rows')
results_df1 = results_df1.loc[results_df1['tran_date'] > datetime(2013, 1, 1)]
#print(results_df1['tran_date'])
#print(results_df1.dtypes)
#results_df1.append(results_df2['contest'])
#results_df1.append(results_df2['cand'])
#results_df1.append(results_df2[''])
results_df1.to_csv('/Users/chrismullins/dev/Public Ethics Comission/compliance queries/CSV/blah1.csv')
#TODO: Personalize save location