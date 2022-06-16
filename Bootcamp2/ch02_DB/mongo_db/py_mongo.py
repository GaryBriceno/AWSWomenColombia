import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["mydatabase"]
my_col = my_db["customers"]


def insert_one(mongo_col, my_dict):
    # Insert my_dict in Mongo
    x = mongo_col.insert_one(my_dict)

    # If you do not specify an _id field,
    # then MongoDB will add one for you and assign a unique id for each document.
    print(x.inserted_id)


def insert_many(mongo_col):
    mylist = [
        {"_id": 1, "name": "John", "address": "Highway 37"},
        {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
        {"_id": 3, "name": "Amy", "address": "Apple st 652"},
        {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
        {"_id": 5, "name": "Michael", "address": "Valley 345"},
        {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
        {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
        {"_id": 8, "name": "Richard", "address": "Sky st 331"},
        {"_id": 9, "name": "Susan", "address": "One way 98"},
        {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
        {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
        {"_id": 12, "name": "William", "address": "Central st 954"},
        {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
        {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]

    x = mongo_col.insert_many(mylist)
    print(x.inserted_ids)


def find_one(mongo_col):
    x = mongo_col.find_one()

    print(x)


def find_all(mongo_col):
    for x in mongo_col.find():
        print(x)


print("Start")
my_dict = {"name": "John", "address": "Highway 37", "main": "john@mail.com"}
insert_one(mongo_col=my_col, my_dict=my_dict)

find_all(mongo_col=my_col)


