# NLP Sentiment Analysis & Users Recommendation on a Bottle Rest API

Chat Analyzer is both a storage system for messaging and a set of tools to produce insights about the chats stored in it. The interaction with both the MongoDB database and the insights tools is through a Bottle based Rest API. The processing tools are developed using NLTK for Natural Language Processing (NLP) and sklearn for the user's affinity recommendation. The API is deployed at Heroku as a Docker Container. To know more, see the documentation below.

API URL: https://chats-analyzer-api.herokuapp.com/

### Documentation:

### 1. User endpoints:

*POST* **"/user/create"**: Create a new user into DB. 
- *Data:* `username`
- *Response:* `user_id : username` 
    - Example of a Response: 
    {"_id": {
        "$oid": "5de7e1dfffe4d3ded588e69f"
        },
    "idUser": 12,
    "userName": "Ms. Potato"
    }


*GET* **"/user/*[iduser]*"**: Get the username of a given userid. 
- *Params:* `iduser`
- *Response:* `iduser`, `username`
    - Example of a Response: 
    {"_id": {
        "$oid": "5de7e1dfffe4d3ded588e69f"
        },
    "idUser": 1,
    "userName": "Mike Wazowski"
    }


*GET* **"/user/*[iduser]*/affinity"**: Get the user id of the three users closest to the requested one. 
- *Data:* `iduser`
- *Response:* `iduser`, `most similar user`
    - Example of a Response: 
    {'1': {
        'recommended_users': [5, 6, 4]
        }
    }


### 2. Chat endpoints:

*POST* **"/chat/newmessage"**: Create a new message on a chat.
- *Data* `iduser`, `idChat`, `datetime`, `text`
- *Response* `idMessage`
    - Example of a Response: 
    {"_id": {
        "$oid": "5de7e2b545a5fcdf690256ad"
        },
        "idUser": 12,
        "idChat": 1,
        "idMessage": 52,
        "datetime": "2019-10-18 12:25:45",
        "text": "Aloha"
    }

*GET* **"/chat/list"**: 
- *Purpose* Get a json object per chatid, with the chatid as key, and an array of the participant idusers.
- *Response* {`idChat` : [`idUser`, `idUser`...]}
    - Example of a Response: 
        [{"0": [0, 1]},
        {"1": [2, 3, 7, 8, 12]},
        {"2": [1, 4]},
        {"3": [0, 5]},
        {"4": [6, 7]}]

*GET* **"/chat/*[idchat]*"**: 
- *Purpose* Get all the messages of a given idchat.
- *Data* `idchat`
- *Response* `iduser`, `idChat`, `idMessage`, `datetime`, `text`
    - Example of a Response: 
    {"_id": {
        "$oid": "5de3b934b4ab0b1e3d241292"
        },
        "idUser": 0,
        "idChat": 0,
        "idMessage": 0,
        "datetime": "2019-10-17 10:15:41",
        "text": "Hey Mike, whats up??"}

*GET* **"/chat/*[idchat]*/sentiment"**: 
- *Purpose:* Get the polarity coefficient of the sum of all messsages on a given chat, and of every user participating in the chat. See [nltk documentation](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentiment#module-nltk.sentiment.sentiment_analyzer) for more information about the coefficients. 
- *Params:* `idchat`
- *Response:* `conversation_polarity`, `users_polarity`
    - Example of a Response: 
    {
        "conversation_polarity": -1.1829,
        "users_polarity": "[{
            "idUser":2,"polarity":-0.7641},{
            "idUser":3,"polarity":-0.4188},{
            "idUser":7,"polarity":0.0},{
            "idUser":8,"polarity":0.0
        }]"
    }