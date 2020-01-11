#! /usr/bin/python3

from bottle import post, get, request, response, run, Bottle
import re
import os
from pymongo import MongoClient
import src.mongodb as mdb  # Local file src/mongodb.py
import src.sentiment_analysis as snt  # Local file src/sentiment_analysis.py
import src.users_affinity as aff  # Local file src/users_affinity.py

# root
@get("/")
def homePage():
    return "Chat Analyser"

# User endpoint
@post("/user/create")
def createUser():
    try:
        userName = request.forms.get("userName")
    except:
        raise KeyError
    return mdb.createUser(userName)


@get("/user/<iduser>")
def getuserName(iduser):
    # get the userName of a given idUser
    return mdb.getuserName(iduser)


@get("/user/<iduser>/affinity")
def getuserAffinity(iduser):
    iduser = int(iduser)
    return aff.mostSimilarUser(iduser)

# Chat endpoint
@post("/chat/newmessage")
def createMessage():
    # extract and validate data
    try:
        idUser = request.forms.get("idUser")
        idchat = request.forms.get('idChat')
        datetime = request.forms.get('datetime')
        text = request.forms.get('text')

    except:
        raise KeyError

    return mdb.newMessage(idUser, idchat, datetime, text)


@get("/chat/list")
def getChatsandParticipants():
    # returns a list of dictionaries with the idchat as key, and the list of iduser per chat as value.
    return mdb.getChatsandParticipants()


@get("/chat/<idchat>")
def getChat(idchat):
    # get all the messages of a given idchat
    return mdb.getChat(idchat)


@get("/chat/<idchat>/sentiment")
def getSentiment(idchat):
    return snt.analyzeSentiment(idchat)


def main():
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    run(host=host, port=port, debug=True)


if __name__ == '__main__':
    main()
