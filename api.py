from bottle import request, response
from bottle import post, get, put, delete
from mongo import MongoClient


### User endpoint
@post("/user/create")
def createUser():
    return

### Chat endpoint
@post("/chat/create")
def createChat():
    return 




if __name__ == '__main__':
    bottle.run(host ='localhost', port = 8000)
