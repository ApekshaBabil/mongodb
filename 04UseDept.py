from pymongo import MongoClient

client=MongoClient("mongodb+srv://apekshababil143:mongodb913@apekcluster.cacaise.mongodb.net/?retryWrites=true&w=majority")
db=client["Office"]
coll=db["Workers"]
dept=input("Enter Dept.: ")
dic={}

dic["Dept"]=dept
print(dic)
for doc in coll.find(dic):
    print(doc)