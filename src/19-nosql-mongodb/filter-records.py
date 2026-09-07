import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# This is where the MongoDB query operators like $in, $gt, $gte, $eq, $lte and $regex finally clicked for me
# result = mycollection.find_one({"name": "Samsung S5"})
# result = mycollection.find_one({"_id": ObjectId("5d6a54e42afaa1169e4b9a0c")})

# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"]
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gt": 2000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gte": 2000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$eq": 2000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$lte": 2000
#     }
# })

# result = mycollection.find({
#     "name": { "$regex": "^S" }
# })


for i in result:
    print(i)


