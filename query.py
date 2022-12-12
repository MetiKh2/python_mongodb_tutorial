import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient['mydatabase']

mycol=mydb['customers']

print('ALL DOCUMENTS')
for x in mycol.find({},{"_id":0,"name":1,'address':1}):
    print(x)
print('_________________________________')

print("FILTERED VALUES")
#myquery={'address':{'$gt':"O"}}
myquery={'address':{'$regex':"^H"}}
mydoc=mycol.find(myquery)
for x in mydoc:
    print(x)

 


