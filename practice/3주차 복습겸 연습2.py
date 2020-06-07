from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

title = db.one.find_one({'title':'매트릭스'})
print(title['star'])

movies = list(db.one.find({'star':title['star']}))
for movie in movies:
    print(movie['title'])

db.one.update_many({'star':title['star']},{'$set':{'star':0}})