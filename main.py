import requests
import json
import csv

scheduleA_api = 'https://data.oaklandca.gov/resource/3xq4-ermg.json'

response = requests.get(scheduleA_api)

scheduleA_dict = response.json()

for item in scheduleA_dict:
    print('filer id: ' + str(item['filer_id']))



#TODO: create a function that prompts user for variable name and returns a csv file containing data


#TODO: google how to export library data to csv file

#def dataSearch():
 #   response_input = requests.get('Enter table name: ')
  #  api_dict = response_input.json()



  #  fieldnames = ['filer_id', 'filer_naml',
   ##     'report_num','committee_type','rpt_date',
     #   'from_date','thru_date','rec_type',
      #  'form_type','tran_id','entity_cd',
       # 'tran_naml','tran_namf','tran_city',
        #'tran_state','tran_zip4','tran_emp',
        #'tran_occ','tran_self','tran_date',
        #'tran_amt1','tran_amt2','intr_self',
        #'memo_refno','tran_location','elect_date']
 #   writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
 #   writer.writeheader()
  #  for item in scheduleA_dict:
  #      writer.writerow(item['filer_id'])
   #     writer.writerow(item['filer_naml'])
    #    writer.writerow(item['report_num'])
      #

with open('data.csv','w',newline='') as csvfile:
    
    datawriter = csv.writer(csvfile,delimiter=' ',quotechar='|',
                                quoting=csv.QUOTE_MINIMAL,)
    datawriter.writerow('FilerID')

    for item in scheduleA_dict:
        datawriter.writerow(item['filer_id'])
