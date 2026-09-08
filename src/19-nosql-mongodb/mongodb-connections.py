# pymongo is the official Python driver for MongoDB, a NoSQL database.
# "NoSQL" means it doesn't organize data into tables/rows with a fixed set
# of columns the way MySQL or SQLite do. Instead, MongoDB stores JSON-like
# "documents" (Python dicts, essentially) grouped into "collections" --
# a collection is roughly what a table is in SQL, and a document is roughly
# what a single row is, except each document can have its own set of fields
# instead of every row being forced to share the exact same columns.
import pymongo

# pymongo.MongoClient(...) opens a connection to a MongoDB server, similar
# to mysql.connector.connect() for MySQL.
#   "mongodb://localhost:27017" (commented out) is how you'd connect to a
#   MongoDB server running on your own machine -- 27017 is MongoDB's default
#   network port, the same idea as MySQL's default port 3306.
# myclient = pymongo.MongoClient("mongodb://localhost:27017")
#
# Replace this with your own MongoDB Atlas connection string (Atlas dashboard -> Connect -> Connect your application)
#
# "mongodb+srv://..." is instead a connection string for MongoDB Atlas,
# MongoDB's official cloud-hosted service -- it bundles the username,
# password, and cluster address into one URL instead of separate host/user/
# password arguments like mysql.connector uses.
myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@<your-cluster-url>/test?retryWrites=true&w=majority")

# A MongoClient can talk to many databases living on the same server; this
# line just picks (and, if it doesn't exist yet, will create on first write)
# the "node-app" database to work with -- similar to picking a database name
# in mysql.connector.connect(database=...).
mydb = myclient["node-app"]

# list_database_names() asks the server for the names of every database it
# currently knows about, so you can double check you're pointed at the right
# server/cluster and see what already exists there.
print(myclient.list_database_names())
