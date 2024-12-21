from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        # Sync Connection
        self.sync_client = MongoClient(os.getenv('MONGO_URI'))
        self.sync_db = self.sync_client[os.getenv('MONGO_DB_NAME')]

        # Async Connection
        self.async_client = AsyncIOMotorClient(os.getenv('MONGO_URI'))
        self.async_db = self.async_client[os.getenv('MONGO_DB_NAME')]

    def get_sync_database(self):
        return self.sync_db

    def get_async_database(self):
        return self.async_db

    def get_ingredients_collection(self, async_mode=False):
        return (self.async_db if async_mode else self.sync_db)['ingredients']

    def get_recipes_collection(self, async_mode=False):
        return (self.async_db if async_mode else self.sync_db)['recipes']

# Singleton instance
db_manager = DatabaseManager()