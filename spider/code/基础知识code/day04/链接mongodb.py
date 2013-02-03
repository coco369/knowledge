
from pymongo import MongoClient

conn = MongoClient('mongodb://127.0.0.1:27017')

db = conn.douban

for movie in db.movie.find():
    print(movie)




