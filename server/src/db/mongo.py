from http import client

from server.config.enviroments import settings
from pymongo import MongoClient

try:
    mongo_url = f'mongodb://{settings.mongo_user}:{settings.mongo_pass}@{settings.mongo_host_port}/?authMechanism=DEFAULT'
    client = MongoClient(mongo_url)
    db = client[settings.mongo_database]
    # user = db.get_collection("user")

except Exception as err:
    print("[ERROR]:",err) 
