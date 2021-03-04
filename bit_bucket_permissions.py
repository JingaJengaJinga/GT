#######################################################################################################
#Program Name   - bit_bucket_permissions.py
#Written By     - Raj Gambhir
#Utility        - The program helps project managers to view permissions on a repo and  
#                  validate if the repo is exposed publically
#######################################################################################################

import  requests
import  json
import  pandas as pd
from    requests.auth import HTTPBasicAuth 
import  getpass


userName = input("Enter user name: ")
userPassword = getpass.getpass("Enter password: ")

projectName = input("Enter project Name: ")
repoName = input("Enter repo name Name: ")

#API to check repo permissions
urlPermissions  = 'http://localhost:8090/rest/api/1.0/projects/' + projectName + '/repos/' + repoName + '/permissions/users'
#API to check if a repo is public
urlPublic       = 'http://localhost:8090/rest/api/1.0/repos?name=' + repoName


rPublic = requests.get(urlPublic, auth=HTTPBasicAuth(userName, userPassword))
jPublic = rPublic.json()

if (rPublic.status_code==200):
    for each in jPublic['values']:
            data9={
                (each['public'])
                }     
            is_public=(each['public'])
else:
    print ("Not a valid response from API call, Please check all input paramters")            
       
        
id_index=[]
project_name = []
repo_name = []

#Print Repo Details
print ("###########################################################")
print ("Project Name = " + projectName)
print ("Repo    Name = " + repoName)
print ("Project PM   = " + userName)

if is_public == True:
    print('The repo ' + repoName + ' is PUBLIC' )
else:
    print('The repo ' + repoName + ' is PRIVATE')

print ("###########################################################")

rPermissions = requests.get(urlPermissions, auth=HTTPBasicAuth(userName, userPassword))

#check if the permissions API call sends a valid response

if (rPermissions.status_code==200):
    jPermissions = rPermissions.json()



    #print(df)
    user_name=[]
    permission = []
    remarks =[]


    #Loop through the permissions data
    for each in jPermissions['values']:
            data1={
                (each['user']['slug'])
                }
            data2={
                (each['permission'])
                } 

            
            #check if the user is an audtior and has a write access
            if (each['user']['slug']).find('aud') != -1 and (each['permission']) != 'REPO_READ' :
                remarks.append("An auditor should not have a WRITE ACCESS")
            #check if transaction banking users have access to core banking    
            elif (urlPermissions.find('COR') != -1 or urlPermissions.find('cor') != -1) and (each['user']['slug']).find('cor') == -1 : 
                remarks.append("ONLY core banking team can have access to core banking repos")    
            else:
                remarks.append('')

            user_name.append(data1)
            permission.append(data2)


    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    pd.options.display.max_rows
    df=pd.DataFrame({"user_name":user_name,"permission":permission,"remarks":remarks})

    #dispaly the data on console
    print(df)
else:
    print ("Not a valid response from API call, Please check all input paramters")

