import requests
#server should be runnig to see the output of this file
response = requests.get('http://127.0.0.1:8000/studentinfo_api/')
print(response.json())