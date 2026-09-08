import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# This is where the MongoDB query operators like $in, $gt, $gte, $eq, $lte and $regex finally clicked for me
#
# Each block below builds a query dict for find()/find_one() and is a
# self-contained example of one MongoDB query operator. Only one of these
# would actually be uncommented and assigned to `result` at a time -- they
# are left here together, commented out, as a reference showing what each
# operator looks like and does. As currently written, every assignment
# below is commented out, so `result` is never actually defined by this
# file -- running it as-is would raise a NameError on the final for-loop.
# In practice you'd uncomment exactly one block to try it out.

# find_one() with a plain dict like {"name": "Samsung S5"} does an exact
# match: it returns the first document where the "name" field is exactly
# equal to "Samsung S5" -- MongoDB's equivalent of
# "select * from products where name = 'Samsung S5' limit 1" in SQL.
# result = mycollection.find_one({"name": "Samsung S5"})

# Looking a document up by its own "_id" field requires wrapping the string
# in ObjectId(...) first, since MongoDB stores _id as a special ObjectId
# type rather than a plain string -- passing the raw string wouldn't match.
# result = mycollection.find_one({"_id": ObjectId("5d6a54e42afaa1169e4b9a0c")})

# $in matches documents where the field's value is any one of the values in
# the given list -- equivalent to SQL's "WHERE name IN ('Samsung S5',
# 'Samsung S6')". This returns every product named either "Samsung S5" or
# "Samsung S6".
# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"]
#     }
# })

# $gt ("greater than") matches documents where price is strictly more than
# 2000 -- equivalent to SQL's "WHERE price > 2000".
# result = mycollection.find({
#     "price": {
#         "$gt": 2000
#     }
# })

# $gte ("greater than or equal to") matches price >= 2000 -- equivalent to
# SQL's "WHERE price >= 2000". Unlike $gt, a product priced at exactly 2000
# would be included here.
# result = mycollection.find({
#     "price": {
#         "$gte": 2000
#     }
# })

# $eq ("equal to") matches price == 2000 exactly -- equivalent to SQL's
# "WHERE price = 2000". This does the same thing as writing
# {"price": 2000} directly; $eq is just the explicit, spelled-out form.
# result = mycollection.find({
#     "price": {
#         "$eq": 2000
#     }
# })

# $lte ("less than or equal to") matches price <= 2000 -- equivalent to
# SQL's "WHERE price <= 2000".
# result = mycollection.find({
#     "price": {
#         "$lte": 2000
#     }
# })

# $regex matches the field's value against a regular expression, similar to
# SQL's LIKE. "^S" means "starts with the letter S" (^ anchors the match to
# the beginning of the string), so this would match "Samsung S5",
# "Samsung S6", etc. -- equivalent to SQL's "WHERE name LIKE 'S%'".
# result = mycollection.find({
#     "name": { "$regex": "^S" }
# })


for i in result:
    print(i)

