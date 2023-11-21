from model import Todo

#mongodb driver
import motor.motor_asyncio

# MongoDB connection settings with username and password
# MONGO_DB_URL = "mongodb://root:root@mongo:27017"
MONGO_DB_URL = "mongodb://root:root@mongo:27017"
DATABASE_NAME = "TodoList"
COLLECTION_NAME = "todo"


# Create an instance of AsyncIOMotorClient
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)

# Reference to the 'TodoList' database and 'todo' collection
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {
        "description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True
