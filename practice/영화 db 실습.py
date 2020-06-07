from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

movie = db.movies.find_one({'title':'매트릭스'})
print(movie['star'])
#db.movies.update_many({'title':'인생은 아름다워'},{'$set':{'star':9.39}})

movies = list(db.movies.find({'star':movie['star']}))
for movie1 in movies:
    print(movie1['title'])
    
db.movies.update_many({'star':movie['star']},{'$set':{'star':0}})