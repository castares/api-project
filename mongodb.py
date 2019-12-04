#!/usr/bin/python3

import os
from pymongo import MongoClient
import getpass
from dotenv import load_dotenv
from bson.json_util import loads, dumps

load_dotenv()

mongodbUrl = os.getenv("MONGODBURL")
client = MongoClient(mongodbUrl)
print(f'Conected to mongodb {mongodbUrl[0:18]}')
db = client['chatsdb']
users = db['users']
messages = db['messages']


def addDocument(collection, document):
    # Standard function to insert documents on MongoDB
    return collection.insert_one(document)


def createUser(userName, collection=users):
    # Add a new username to MongoDB users Collection
    if userName in users.distinct("userName"):
        raise NameError(f"userName already exists")
    else:
        user = {
            'idUser': max(users.distinct("idUser"))+1,
            'userName': userName
        }
        addDocument(collection, user)
        return dumps(collection.find({'userName': userName}))


def newMessage(idUser, idchat, datetime, text, collection=messages):
    # Add a new messa to MongoDB messages Collection
    if int(idUser) not in users.distinct("idUser"):
        raise NameError(
            f"idUser doesn't exists. Create user before adding messages.")
    idMessage = max(messages.distinct("idMessage"))+1
    message = {
        'idUser': int(idUser),
        'idChat': int(idchat),
        'idMessage': idMessage,
        'datetime': datetime,
        'text': text
    }
    addDocument(collection, message)
    return dumps(collection.find({'idMessage': idMessage}))


def allMessages():
    return messages.find({}, {'idUser': 1, 'text': 1})


def getChat(idchat, collection=messages):
    return dumps(collection.find({'idChat': int(idchat)}))


def getuserName(idUser, collection=users):
    return dumps(collection.find({'idUser': int(idUser)}))


def main():
    # Connect to DB
    mongodbUrl = os.getenv("MONGODBURL")
    print(f'Conected to mongodb {mongodbUrl[0:8]}')

    # define Client, Database and collections on that database
    client = MongoClient(mongodbUrl)
    # create database
    db = client['chatsdb']
    collist = db.list_collection_names()
    # Create New Collections
    new_collections = ["users", "messages"]
    for coll in new_collections:
        if coll not in collist:
            db.create_collection(coll)
            print(f"collection {coll} created")
        else:
            print(f"Collection {coll} already exists")


if __name__ == "__main__":
    main()
