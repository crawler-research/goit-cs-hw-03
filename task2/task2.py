from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["MaksymDB"]
collection = db["cats"]

# Create db structure
def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    collection.insert_one(cat)

# Read
def get_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def get_cat_by_name(name):
    cat = collection.find_one({"name": name})
    print(cat)

# Update
def update_cat_age(name, age):
    collection.update_one({"name": name}, {"$set": {"age": age}})

def add_feature_to_cat(name, feature):
    collection.update_one({"name": name}, {"$push": {"features": feature}})

# Delete
def delete_cat_by_name(name):
    collection.delete_one({"name": name})

def delete_all_cats():
    collection.delete_many({})