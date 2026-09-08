import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# Print every document currently in the collection, before the update, so
# we can compare it against the printout at the bottom of the file.
for i in mycollection.find():
    print(i)

# update_one(filter, update) would find the FIRST document matching
# `filter` and apply `update` to just that one document -- MongoDB's rough
# equivalent of a SQL UPDATE with a WHERE clause and no LIMIT concerns,
# since here it's explicitly limited to a single document by definition.
# '$set' is a MongoDB update operator meaning "overwrite these specific
# fields with these new values, leave every other field on the document
# untouched" -- without $set, an update payload would instead try to
# replace the ENTIRE document.
# mycollection.update_one(
#     {'name': 'Samsung S6'},
#     {'$set': {
#         'name': 'IPhone 7',
#         'price': 5000
#     }}
# )

# `query` is the filter that decides WHICH documents get updated -- only
# documents where the "name" field equals 'Samsung S7'.
query = {'name': 'Samsung S7'}

# `newvalues` describes WHAT changes to apply: $set here overwrites just the
# name and price fields on each matched document, leaving any other fields
# (like "categories" from creating-collections.py) exactly as they were.
newvalues = {'$set': {
                'name': 'IPhone 8',
                'price': 5000
            }}

# update_many(filter, update), unlike update_one(), applies the change to
# EVERY document matching the filter, not just the first one -- the
# equivalent of a SQL UPDATE ... WHERE that can affect more than one row.
result = mycollection.update_many(query, newvalues)

# .modified_count is how many documents were actually changed by the
# update -- MongoDB's equivalent of cursor.rowcount after a SQL UPDATE.
print(f'{result.modified_count} record(s) updated.')

# Print the collection again so the change made above is visible.
for i in mycollection.find():
    print(i)
