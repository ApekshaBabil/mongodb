from pymongo import MongoClient

client=MongoClient("mongodb+srv://apekshababil143:mongodb913@apekcluster.cacaise.mongodb.net/?retryWrites=true&w=majority")
db=client["Office"]
coll=db["Workers"]

wid=input("Enter Workers ID: ")
dic={}
dic["_id"]=wid
print(dic)
for doc in coll.find(dic):
    print(doc)