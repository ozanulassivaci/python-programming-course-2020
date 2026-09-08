import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# Show what's in the collection before deleting anything, for comparison
# against the printout at the bottom of the file.
for i in mycollection.find():
    print(i)

print('*'*50)

# delete_one(filter) removes just the FIRST document matching the filter --
# MongoDB's equivalent of a SQL DELETE that's guaranteed to affect at most
# one row.
# mycollection.delete_one({"name":"IPhone 8"})

# delete_many(filter) removes EVERY document matching the filter. Combined
# with the $regex operator (pattern matching, similar to SQL's LIKE), this
# line would delete every product whose name starts with "S".
# mycollection.delete_many({"name": {"$regex":"^S"}})

# delete_many({}) with an EMPTY filter dict matches every document in the
# collection -- so this deletes everything, the MongoDB equivalent of
# running SQL's "DELETE FROM products" with no WHERE clause at all. Just
# like that SQL statement, this is destructive and irreversible once it
# runs (there's no built-in undo), so an empty filter here should be used
# deliberately, not by accident.
result = mycollection.delete_many({})

# .deleted_count reports how many documents were actually removed --
# MongoDB's equivalent of cursor.rowcount after a SQL DELETE.
print(f'{result.deleted_count} record(s) deleted.')

# The collection should now be empty, so this loop prints nothing.
for i in mycollection.find():
    print(i)
