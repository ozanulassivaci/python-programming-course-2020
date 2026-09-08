import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

# Pick (and create on first write, if it doesn't already exist) the
# "node-app" database.
mydb = myclient["node-app"]
# A collection is MongoDB's equivalent of a SQL table: a named group of
# documents. Just like the database above, you don't need to explicitly
# "create" it first -- indexing into mydb with a name that doesn't exist yet
# (mydb["products"]) simply gives you a handle that will create the
# collection automatically the moment you first insert something into it.
mycollection = mydb["products"]

# insert_one() adds a single document -- a Python dict -- to the collection.
# Unlike a SQL table, there's no schema to define up front: you don't need
# to declare "products has columns name and price" anywhere before writing
# this. Whatever keys the dict has become that document's fields.
# product = {"name":"Samsung S5", "price": 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# insert_one() returns an InsertOneResult object; .inserted_id is the unique
# identifier MongoDB automatically generated for the new document (stored in
# its "_id" field) -- conceptually similar to an auto-incrementing primary
# key in SQL, except it's a special ObjectId value rather than a plain
# integer.
# print(result.inserted_id)


# This is where I learned insert_many() can take a list of dicts, and that each dict doesn't need the same fields
#
# insert_many() adds several documents in a single call, similar to
# executemany() for SQL inserts. Notice that the two dicts below don't share
# the same set of keys -- the first has "description" and the second has
# "categories" instead -- and that's perfectly valid in MongoDB. Every
# document in a collection is independent; there's no requirement that they
# all have the same fields the way every row in a SQL table must have the
# same columns.
productList = [
    {"name":"Samsung S6", "price": 3000, "description":"a good phone"},
    {"name":"Samsung S7", "price": 4000, "categories": ['phone','electronics']}
]

result = mycollection.insert_many(productList)
# .inserted_ids is a list of the auto-generated ids for every document that
# was just inserted, in the same order as productList.
print(result.inserted_ids)
