#######################################################################################################
#Program Name   - bit_bucket_permissions.py
#Written By     - Raj Gambhir
#Utility        - The program helps project managers to view list of repos  
#                  
#######################################################################################################

import  requests
import  json
import  pandas as pd
from    requests.auth import HTTPBasicAuth 
import  getpass


userName = input("Enter user name: ")
userPassword = getpass.getpass("Enter password: ")

#API to get list of repos
urlPublic       = 'http://localhost:8090/rest/api/1.0/repos'


rPublic = requests.get(urlPublic, auth=HTTPBasicAuth(userName, userPassword))
jPublic = rPublic.json()



rPermissions = requests.get(urlPublic, auth=HTTPBasicAuth(userName, userPassword))

#check if the permissions API call sends a valid response

if (rPublic.status_code==200):
    jPublic = rPublic.json()



    #print(df)
    repo_name=[]
    project_name = []
    project_key = []
    isPublic =[]


    #Loop through the permissions data
    for each in jPublic['values']:
            data1={
                (each['slug'])
                }
            data2={
                (each['project']['name'])
                } 
            data3={
                (each['public'])
                } 
            data4={
                (each['project']['key'])
                }     
            


            repo_name.append(data1)
            project_name.append(data2)
            isPublic.append(data3)
            project_key.append(data4)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    pd.options.display.max_rows
    df=pd.DataFrame({"project_name":project_name,"project_key":project_key,"repo_name":repo_name,"isPublic":isPublic})

    #dispaly the data on console
    print(df)
else:
    print ("Not a valid response from API call, Please check all input paramters")

