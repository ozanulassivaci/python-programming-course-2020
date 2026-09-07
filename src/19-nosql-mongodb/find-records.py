import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one()
for i in mycollection.find({},{"_id":0 ,"name": 1}):
    print(i)

# print(result)
