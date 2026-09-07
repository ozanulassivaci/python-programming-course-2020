import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort('name', -1)
# result = mycollection.find().sort('price', -1)
# result = mycollection.find().sort([('name',1), ('price',-1)])

for i in result:
    print(i)

