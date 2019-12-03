# NLP Sentiment Analysis & Users Recommendation on a Bottle Rest API

This API has been developed as a project on Ironhack's Data Analytics bootcamp. We've created a rest API using Bottle Framework linked to a MongoDB database stored in MongoDB Atlas. 

Using nltk and sklearn the API returns sentiment analysis and users affinity recommendation from the available chats on 

The API is available online at Heroku from a Docker image. See Documentation below.


URL: https://chats-analyser-api.herokuapp.com/

### Documentation:

#### Endpoint /user: 

*GET* /user/create 

- data=username
- userid will be assigned automatically.

