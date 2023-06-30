from pymongo import MongoClient

client=MongoClient("mongodb+srv://apekshababil143:mongodb913@apekcluster.cacaise.mongodb.net/?retryWrites=true&w=majority")
db=client["Office"]
coll=db["Workers"]

wid=input("Enter Worker ID: ")
nm=input("Enter Employee Name: ")
dp=input("Enter Dept.: ")
po=input("Enter Post: ")
ct=input("Enter City: ")
sal=float(input("Enter Salary: "))
mob=int(input("Enter Mobile Number: "))
email=input("Enter Email ID: ")


dic={}
dic['_id']=wid
dic['Name']=nm
dic['Dept']=dp
dic['Post']=po
dic['City']=ct
dic['Salary']=sal
dic['Mobile Number']=mob
dic['Email ID']=email

print(dic)

coll.insert_one(dic)
print("Document added to workers collection.")