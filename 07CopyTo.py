from pymongo import MongoClient

client=MongoClient("mongodb+srv://apekshababil143:mongodb913@apekcluster.cacaise.mongodb.net/?retryWrites=true&w=majority")
db=client["Office"]
coll=db["Workers"]
newcol=db["Exworkers"]

wid=input('Enter Workers Id: ')
qr={}
qr['_id']=wid
print(qr)


for doc in coll.find(qr):
    print(doc)
    

newcol.insert_one(doc)
print("Document copied into Exworkers Collection.")

coll.delete_one(doc)
print("Delete from Workers Collection Successfully.")
