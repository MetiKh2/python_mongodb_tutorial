import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient['mydatabase']

mycol=mydb['customers']

print('ALL DOCUMENTS')
for x in mycol.find({},{"_id":0,"name":1,'address':1}):
    print(x)
print('_________________________________')

mydoc=mycol.find().sort('name',-1)
for x in mydoc:
    print(x)

