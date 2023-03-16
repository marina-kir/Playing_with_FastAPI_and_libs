import pymongo

from pymongo import MongoClient

client = MongoClient()

# client = MongoClient('localhost', 27017)
#
# client = MongoClient('mongodb://localhost:27017/')

db = client.local
col = db.marina

import pprint
from bson.objectid import ObjectId
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"]}
# post_id = col.insert_one(post).inserted_id
pprint.pprint(col.find_one({"_id": ObjectId("63921390753b2839bdffaed3")}, {"a"}))
pprint.pprint(col.find_one({"a":5}))
if (pprint.pprint(col.find_one({"q":5})) == None):
    print ("1")
pass




