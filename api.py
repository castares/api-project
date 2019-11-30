from bottle import post, get, request, response, run
import mongodb as mdb
from bson.json_util import loads, dumps
import os
from pymongo import MongoClient


# Connect to MongoDB Atlas:
mongodbUrl = os.getenv("MONGODBURL")
client = MongoClient(mongodbUrl)
db = client['chatsdb']
users_coll = db['Users']
messages_coll = db['Messages']
users = mdb.CollConnection(os.getenv('MONGODBURL'), 'chatsdb', 'Users')
messages = mdb.CollConnection(os.getenv('MONGODBURL'), 'chatsdb', 'Messages')


# User endpoint
@post("/user/create")
def createUser():
    # extract and validate user
    try:
        userid = request.forms.get("idUser")
        username = request.forms.get('userName')

    except:
        raise ValueError

    if userid in users_coll.distinct("userid"):
        raise ValueError
    else:
        # insert document to mongo collection.
        return {
            "inserted_user_id": str(users.newUser(userid, username))}

# Chat endpoint
@post("/message/create")
def createMessage():
     # extract and validate user
    try:
        userid = request.forms.get("idUser")
        chatid = request.forms.get('idChat')
        messageid = request.forms.get('idMessage')
        datetime = request.forms.get('datetime')
        text = request.forms.get('text')

    except:
        raise ValueError

    # insert document to mongo collection.
    return {
        "inserted_user_id": str(messages.newMessage(userid, chatid, messageid, datetime, text))
    }


@get("/messages/<chatid>")
def getChat(chatid):
    print(f'chat id: {chatid}')
    return dumps(messages_coll.find({'idChat': str(chatid)}))

# TODO REVIEW THIS!!!
@get("/user/<user_ids>")
def getUsers(user_ids):
    return dumps(users_coll.find({'userid': {"$in": ["0", "1"]}})))


def main():
    # run(host='localhost', port=8000)
    print(dumps(users_coll.find({'userid': {"$in": ["0", "1"]}})))


if __name__ == '__main__':
    main()
