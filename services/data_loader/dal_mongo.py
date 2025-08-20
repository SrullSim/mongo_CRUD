from pymongo import MongoClient


class DAL_mongo:

    def __init__(self, host, database, collection, user= None, password= None):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = self.open_connection()


    def get_URI(self):
        if self.user and self.password:
            URI = f"mongodb://{self.user}:{self.password}@{self.host}::27017"
        else:
            URI = f"mongodb://{self.user}:27017"

        return URI


    def open_connection(self):
        try:
            client = MongoClient(self.URI)
        except Exception as e:
            print("Error: ", e)
            client = None

        return client


    def get_all(self):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            data = collection.find()
            return data



    def delete_one(self, id):
        if self.client:
            db = self.client[self.database]
            collection = db[self.collection]
            collection.delete_one({'id': id})



