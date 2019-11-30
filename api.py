from bottle import post, get, request, response, run
import mongodb as mdb
import bson
import os


# User endpoint
@post("/user/create")
def createUser():
    # extract and validate user
    try:
        userid = request.forms.get("idUser")
        username = request.forms.get('userName')

    except:
        raise ValueError

    # insert document to mongo collection.
    return {"inserted_user_id": str(users.newUser(userid, username))}

# # Chat endpoint
# @post("/chat/create")
# def createChat():
#     return


def main():
    users.
    run(host='localhost', port=8000)


if __name__ == '__main__':
    main()
