import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# .sort(...) orders the documents a find() query returns, the same idea as
# ORDER BY in SQL. find() with no arguments matches every document (like a
# SELECT with no WHERE clause), and .sort() is then chained onto it to
# control the order results come back in.
#
# sort('name', -1) sorts by the "name" field in descending order (Z-to-A).
# The second argument is the sort direction: 1 means ascending (A-to-Z /
# smallest-to-largest), -1 means descending (Z-to-A / largest-to-smallest).
# result = mycollection.find().sort('name', -1)

# sort('price', -1) sorts by price from highest to lowest.
# result = mycollection.find().sort('price', -1)

# Passing a list of (field, direction) tuples sorts by multiple fields at
# once, the same idea as SQL's "ORDER BY name, price DESC": sort by name
# ascending first, and for any documents that share the same name, use
# price (descending) to break the tie.
# result = mycollection.find().sort([('name',1), ('price',-1)])

# Only one of the sort() calls above would be uncommented at a time; as
# written here they're all commented out, so `result` is never actually
# assigned and this loop would raise a NameError if run as-is -- uncomment
# one line above to try it.
for i in result:
    print(i)
