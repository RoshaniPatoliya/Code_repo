import pymongo
myclient = pymongo.mongoclient('mongodb://localhost: 27017')
database = myconnect['database']
print(myclient.list_database_names())