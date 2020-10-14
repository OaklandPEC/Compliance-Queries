import requests
import json
import csv
from csv import reader
from csv import writer

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


with open('data.csv','w',newline='') as csvfile:
    fieldnames = 'Filer_ID','Filer_NamL','Report_Num','Committee_Type','Rpt_Date','From_Date','Thru_Date','Elect_Date','tblCover_Office_Cd','tblCover_Offic_Dscr','Rec_Type','Form_Type','Tran_ID','Entity_Cd','Tran_NamL','Tran_NamF','Tran_NamT','Tran_NamS','Tran_Adr1','Tran_Adr2','Tran_City','Tran_State','Tran_Zip4','Tran_Emp','Tran_Occ','Tran_Self','Tran_Type','Tran_Date','Tran_Date1','Tran_Amt1','Tran_Amt2','Tran_Dscr','Cmte_ID','Tres_NamL','Tres_NamF','Tres_NamT','Tres_NamS','Tres_Adr1','Tres_Adr2','Tres_City','Tres_State','Tres_Zip','Intr_NamL','Intr_NamF','Intr_NamT','Intr_NamS','Intr_Adr1','Intr_Adr2','Intr_City','Intr_State','Intr_Zip4','Intr_Emp','Intr_Occ','Intr_Self','Cand_NamL','Cand_NamF','Cand_NamT','Cand_NamS','tblDetlTran_Office_Cd','tblDetlTran_Offic_Dscr','Juris_Cd','Juris_Dscr','Dist_No,Off_S_H_Cd','Bal_Name','Bal_Num,Bal_Juris','Sup_Opp_Cd','Memo_Code','Memo_RefNo','BakRef_TID','XRef_SchNm','XRef_Match','Loan_Rate','Int_CmteId','Tran_Location','Tres_Location','Intr_Location'
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    #works up to here
    #for item in scheduleA_dict:
    writer.writerow(item['filer_id'])
    writer.writerow(item['filer_naml'])
    writer.writerow(item['report_num'])
      #

#with open('data.csv','r',newline='') as csvoutput:
 #   with open('data.csv','w',newline='') as csvfile:
  #      datareader = csv.reader(csvoutput)
   #     datawriter = csv.writer(csvfile,delimiter=' ',quotechar='|',
   #                             quoting=csv.QUOTE_MINIMAL,)
    #datawriter.writerow('FilerID')
    ###      
       ##    row.append('hey')
         #   datawriter.writerow(row)

      
