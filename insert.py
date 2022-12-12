import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient['mydatabase']

mycol=mydb['customers']

#doc={'name':'john','address':'Highway 37'}

#x=mycol.insert_one(doc)

#print(x.inserted_id)

#mylist=[
#    {'name':'Amy','address':'Apple st 652'},
#    {'name':'Sandy','address':'Valley 345'},
#    {'name':'Betty','address':'Park lane 38'}
#    ]
doc={"_id":1,'name':'Hannah','address':'One way 98'}
x=mycol.insert_one(doc)
print(x.inserted_id)



