import pymongo
# ObjectId lets us build the special id type MongoDB uses for its automatic
# "_id" field, so we can look a document up by that id (see filter-records.py
# for an example: ObjectId("5d6a54e42afaa1169e4b9a0c")).
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# find_one() would return just the first matching document as a single
# dict (or None if nothing matches) -- MongoDB's rough equivalent of SQL's
# fetchone().
# result = mycollection.find_one()

# find(query, projection) is MongoDB's equivalent of a SQL SELECT. It
# returns a "cursor" you can loop over to get each matching document, one at
# a time, similar to iterating over cursor.fetchall() in SQL.
#   - The first argument, {}, is the query filter -- an empty dict means
#     "no conditions, match every document in the collection" (like a SQL
#     query with no WHERE clause).
#   - The second argument, {"_id": 0, "name": 1}, is the projection: it
#     controls which fields come back in each result, the same idea as
#     listing specific column names after SELECT instead of using *.
#     A value of 1 means "include this field", and 0 means "exclude this
#     field". Here, "_id": 0 explicitly hides MongoDB's automatic _id field
#     (which is included by default otherwise), and "name": 1 asks for only
#     the name field -- so each printed document will just be
#     {"name": "..."} rather than the whole product record.
for i in mycollection.find({},{"_id":0 ,"name": 1}):
    print(i)

# print(result)
