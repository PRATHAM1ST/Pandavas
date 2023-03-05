import pymongo
import datetime

# MongoDB Atlas connection string
connection_string = "mongodb+srv://pratham:vzLMUHDAX9Q4hCo3@cluster0.9cginxy.mongodb.net/Plates?retryWrites=true&w=majority"

# Connect to MongoDB Atlas cluster
client = pymongo.MongoClient(connection_string)

# Select database and collection
db = client['Plates']
collection = db['Data']

# Sample car data
car_data = {
    "license_plate": "ABC123",
    "timestamp": datetime.datetime.now(),
    "location": {
        "latitude": 37.7749,
        "longitude": -122.4194
    },
    "other_details": "Some other details"
}

# Insert car data into MongoDB Atlas collection
collection.insert_one(car_data)

# Close MongoDB Atlas connection
client.close()
