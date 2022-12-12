import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient['mydatabase']

mycol=mydb['customers']
#mycol.insert_one({'name': 'Sarah', 'address': 'Highway 38'})
print('ALL DOCUMENTS')
for x in mycol.find({},{"_id":0,"name":1,'address':1}):
    print(x)
print('_________________________________')

myquery={'address':{'$regex':'^H'}}
x=mycol.delete_many({})
print(x.deleted_count,'documents deleted.')


