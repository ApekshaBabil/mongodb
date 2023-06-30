from pymongo import MongoClient

client=MongoClient("mongodb+srv://apekshababil143:mongodb913@apekcluster.cacaise.mongodb.net/?retryWrites=true&w=majority")
db=client["Office"]
coll=db["Workers"]


for doc in coll.find():
    print(doc)

