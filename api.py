#! /usr/bin/python3

from bottle import post, get, request, response, run, Bottle
import re
import os
from pymongo import MongoClient
import mongodb as mdb


# User endpoint
@post("/user/create")
def createUser():
    # extract and validate user
    try:
        idUser = request.forms.get("idUser")
        userName = request.forms.get('userName')

    except:
        raise ValueError

    # insert user to mongo collection.
    return mdb.newUser(idUser, userName)


@get("/user/<idUser>")
def getuserName(idUser):
    # get the userName of a given idUser
    return mdb.getuserName(idUser)

# TODO: response to post requests.


# Chat endpoint

@post("/message/create")
def createMessage():
     # extract and validate user
    try:
        idUser = request.forms.get("idUser")
        chatid = request.forms.get('idChat')
        idMessage = request.forms.get('idMessage')
        datetime = request.forms.get('datetime')
        text = request.forms.get('text')

    except:
        raise ValueError

    # insert document to mongo collection.
    return mdb.newMessage(idUser, chatid, idMessage, datetime, text)


@get("/messages/<chatid>")
def getChat(chatid):
    # get all the messages of a given chatid
    return mdb.getChat(chatid)


def main():
    run(host='localhost', port=8000)


if __name__ == '__main__':
    main()


# TODO REVIEW THIS!!!
# # Bottle Object to process a list of numbers as a wildcard filter.
# routelist = Bottle()

# def list_filter(config):
#     ''' Matches a comma separated list of numbers. '''
#     delimiter = config or ','
#     regexp = r'\d+(%s\d)*' % re.escape(delimiter)

#     def to_python(match):
#         return map(int, match.split(delimiter))

#     def to_url(numbers):
#         return delimiter.join(map(str, numbers))

#     return regexp, to_python, to_url


# routelist.router.add_filter('list', list_filter)

# @routelist.route('/user/<ids:list>', method=['GET'])
# def userNames(ids):
#     return dumps(users_coll.find({'idUser': {"$in": ids}}))
