from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

db=client['test']
sub=db['sub']

# value={"name":"悟空"}
# insert=sub.insert_one(value)
# print(insert)
s=sub.find_one()
print(s)