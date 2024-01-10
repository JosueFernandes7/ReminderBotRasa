from pymongo import MongoClient
from config import settings

class MongoDBConnection:
    def __init__(self, db_name=None):
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(settings.DB_URL)
            if self.db_name:
                self.db = self.client[self.db_name]
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def disconnect(self):
        try:
            if self.client:
                self.client.close()
                print("Disconnected from MongoDB")
        except Exception as e:
            print(f"Error disconnecting from MongoDB: {e}")
