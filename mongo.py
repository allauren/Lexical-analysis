import pymongo

client = pymongo.MongoClient("mongodb+srv://allauren:0704KxiO@cluster0-bn9x1.gcp.mongodb.net/test?retryWrites=true")

db = client.joe
coll = db.oregon

for document in coll.find():
    print (document)
    break