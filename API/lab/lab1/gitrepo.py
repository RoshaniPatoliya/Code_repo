
import requests
json_str = requests.get("https://api.github.com/users/RoshaniPatoliya/repos")
data = json_str.json()
for name in data:
    print(f"RepoName : {name['name']}")
    '''
print("\nValues in repo: ", data[1]['name'])



import requests
response = requests.get('https://api.github.com/users/RoshaniPatoliya/repos')
my_repos = response.json()
for repo in my_repos:
    print(f"RepoName : {repo['name']}")
    

import json
geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
geek_dict = json.loads(geek)
 
# printing all elements of dictionary
print("Dictionary after parsing: ", geek_dict)
 
# printing the values using key
print("\nValues in Languages: ", geek_dict['Languages'])

import  requests
import json
endpoint="https://github.com/arunbhalli?tab=repositories"
get_response = requests.get(endpoint)
data = json.loads(get_response.json())

import requests
endpoint="https://github.com/arunbhalli?tab=repositories"
get_response = requests.get(endpoint)
print(get_response.json())'''

