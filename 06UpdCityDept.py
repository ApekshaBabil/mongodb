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


newct=input('Enter New City: ')
newdp=input('Enter New Dept: ')
ch={}
ch['City']=newct
ch['Dept']=newdp
print(ch)

upd={'$set':ch}
print(upd)

coll.update_one(qr,upd)
print('City and Dept. updated Successfully.')
for doc in coll.find(qr):
    print(doc)