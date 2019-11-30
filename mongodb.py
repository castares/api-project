#!/usr/bin/python3

import os
from pymongo import MongoClient
import getpass
from dotenv import load_dotenv


load_dotenv()


class CollConnection:

    def __init__(self, connectionurl, db, collection):
        self.client = MongoClient(connectionurl)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def addDocument(self, document):
        a = self.collection.insert_one(document)
        print("Inserted", a.inserted_id)
        return a.inserted_id

    def newUser(self, userid, username):
        document = {
            'userID': userid,
            'username': username
        }
        return self.addDocument(document)

    def newMessage(self, userid, chatid, messageid, datetime, text):
        document = {
            'userID': userid,
            'ChatID': chatid,
            'MessageID': messageid,
            'datetime': datetime,
            'text': text
        }
        return self.addDocument(document)


def main():
    # Connect to DB
    mongodbUrl = os.getenv("MONGODBURL")
    print(f'Conected to mongodb {mongodbUrl}')

    # define Client, Database and collections on that database
    client = MongoClient(mongodbUrl)
    db = client['chatsdb']
    collist = db.list_collection_names()

    # Create New Collections
    new_collections = ["Users", "Messages"]
    for coll in new_collections:
        if coll not in collist:
            db.create_collection(coll)
        else:
            print(f"Collection {coll} already exists")


if __name__ == "__main__":
    main()
