# NLP Sentiment Analysis & Users Recommendation on a Bottle Rest API

I developed this project on Ironhack's Data Analytics bootcamp. The goals of the project are: 

- (L1🧐) Write an API in bottle just to store chat messages in a database like mongodb or mysql.
- (L2🥳) Extract sentiment from chat messages and perform a report over a whole conversation
- (L3😎) Deploy the service with docker to heroku and store messages in a cloud database.
- (L4🤭) Recommend friends to a user based on the contents from chat `documents` using a recommender system with `NLP` 

To achieve those goals, I have created a rest API using Bottle Framework, linked to a MongoDB database stored in MongoDB Atlas. 

Using nltk and sklearn, the app produces chat sentiment analysis and users affinity recommendation.

The API is available online at Heroku. See Documentation below.

URL: https://chats-analyzer-api.herokuapp.com/

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

**GET** **"/user/[iduser]"**: Get the username of a user id. 
- *Params:* `iduser`
- *Response:* `iduser`, `username`
    - Example of a Response: 
    {"_id": {
        "$oid": "5de7e1dfffe4d3ded588e69f"
        },
    "idUser": 1,
    "userName": "Mike Wazowski"
    }


**GET** **"/user/[iduser]/affinity"**: Get the user id of the most similar user to the requested one. 
- *Data:* `iduser`
- *Response:* `iduser`, `most similar user`
    - Example of a Response: 
    {
        {"iduser": 
            "7"}: 
            {"most similar user": 
                "5")}
    }


### 2. Chat endpoints:

**POST** **"/chat/newmessage"**: Create a new message on a chat.
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

**GET** **"/chat/<idchat>"**: 
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

**GET** **"/chat/<idchat>/sentiment"**: 
- *Purpose* Get the polarity coefficient of the sum of all messsages on a given chat, and of every user participating in the chat. See [nltk documentation](https://www.nltk.org/api/nltk.sentiment.html?highlight=sentiment#module-nltk.sentiment.sentiment_analyzer) for more information about the coefficients. 
- *Params* `idchat`
- *Response* `conversation_polarity`, `users_polarity`
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