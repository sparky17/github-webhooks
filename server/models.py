from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
print(f'client is ${client}')
db = client["github_events"] 
events = db.events
