import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

# mycollection.update_one(
#     {'name': 'Samsung S6'},
#     {'$set': {
#         'name': 'IPhone 7',
#         'price': 5000
#     }}
# )
query = {'name': 'Samsung S7'}

newvalues = {'$set': {
                'name': 'IPhone 8',
                'price': 5000
            }}

result = mycollection.update_many(query, newvalues)

print(f'{result.modified_count} record(s) updated.')

for i in mycollection.find():
    print(i)
