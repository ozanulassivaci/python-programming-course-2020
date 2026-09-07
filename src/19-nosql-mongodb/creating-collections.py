import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# product = {"name":"Samsung S5", "price": 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)


# This is where I learned insert_many() can take a list of dicts, and that each dict doesn't need the same fields
productList = [
    {"name":"Samsung S6", "price": 3000, "description":"a good phone"},
    {"name":"Samsung S7", "price": 4000, "categories": ['phone','electronics']}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)
