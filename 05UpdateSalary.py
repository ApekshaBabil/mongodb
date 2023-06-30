from pymongo import MongoClient

client=MongoClient("mongodb+srv://apekshababil143:mongodb913@apekcluster.cacaise.mongodb.net/?retryWrites=true&w=majority")
db=client["Office"]
coll=db["Workers"]


wid=input('Enter Workers Id: ')
qr={}
qr['_id']=wid

print(qr)
for doc in coll.find(qr):
    print(doc)


newsal=float(input('Enter New Salary: '))
ch={}
ch['Salary']=newsal
print(ch)

upd={'$set':ch}
print(upd)

coll.update_one(qr,upd)
print('Salary updated Successfully.')
for doc in coll.find(qr):
    print(doc)
