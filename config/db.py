from pymongo import MongoClient

mongodb_host = "localhost"
mongodb_port = 27017

# Creating a MongoClient with explicit connection details
conn = MongoClient(host=mongodb_host, port=mongodb_port)
