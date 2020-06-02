# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:45:54 2020

@author: Bitan
"""

import requests
import pandas as pd

#Patient Level : Raw Data Partition 1 
response1 = requests.get("https://api.covid19india.org/raw_data1.json")
data1 = response1.json()
data11 = data1['raw_data']
df1 = pd.DataFrame(data11)
df1.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\raw_data_1.xlsx",index=False)
       
#Patient Level : Raw Data Partition 2
response2 = requests.get("https://api.covid19india.org/raw_data2.json")
data2 = response2.json()
data22 = data2['raw_data']
df2 = pd.DataFrame(data22)
df2.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\raw_data_2.xlsx",index=False)
       
#Patient Level : Raw Data Partition 3
response3 = requests.get("https://api.covid19india.org/raw_data3.json")
data3 = response3.json()
data33 = data3['raw_data']
df3 = pd.DataFrame(data33)
df3.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\raw_data_3.xlsx",index=False)
       
#National Level :Time series, State-wise stats and Test counts
response4 = requests.get("https://api.covid19india.org/data.json")
data4 = response4.json()
data44_1 = data4['cases_time_series']
data44_2 = data4['statewise']
data44_3 = data4['tested']
df4_1 = pd.DataFrame(data44_1)
df4_2 = pd.DataFrame(data44_2)
df4_3 = pd.DataFrame(data44_3)
df4_1.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\National Level1.xlsx",sheet_name="cases_time_series",index=False)
df4_2.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\National Level2.xlsx",sheet_name="statewise",index=False)
df4_3.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\National Level3.xlsx",sheet_name="tested",index=False)      

#State Level : has district-wise info
response5 = requests.get("https://api.covid19india.org/state_district_wise.json")
data5 = response5.json()
data55 = [(k, v) for k, v in data5.items()]
df5 = pd.DataFrame(data55)
df5.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\State Level.xlsx",index=False)
       
#State Level : has district-wise info V2
response6 = requests.get("https://api.covid19india.org/v2/state_district_wise.json")
data6 = response6.json()
data66 = [(k, v) for k, v in data6.items()]
df6 = pd.DataFrame(data66)
df6.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\State Level_v2.xlsx",index=False)
       
#State Level : Daily changes
response7 = requests.get("https://api.covid19india.org/states_daily.json")
data7 = response7.json()
data77 = data7['states_daily']
df7 = pd.DataFrame(data77)
df7.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\State Level Daily changes.xlsx",index=False)
       

#State Level : Testing data
response8 = requests.get("https://api.covid19india.org/state_test_data.json")
data8 = response8.json()
data88 = data8['states_tested_data']
df8 = pd.DataFrame(data88)
df8.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\State Level Testing data.xlsx",index=False)
      
#Essentials and resources
response9 = requests.get("https://api.covid19india.org/resources/resources.json")
data9 = response9.json()
data99 = data9['resources']
df9 = pd.DataFrame(data99)
df9.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\Essentials and resources.xlsx",index=False)
      
#District Zones	
response10 = requests.get("https://api.covid19india.org/zones.json")
data10 = response10.json()
data100 = data10['zones']
df10 = pd.DataFrame(data100)
df10.to_excel("E:\\ACROALIAS\\COVID-19\\COVID-19\\API\\PROD_Codes_COVID-19\\Data\\District Zones.xlsx",index=False)
      



