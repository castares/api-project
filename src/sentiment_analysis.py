import json
from bson.json_util import loads, dumps
import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Local Files
from .mongodb import getChat  # This project file mongodb.py

nltk.download("vader_lexicon")
sid = SentimentIntensityAnalyzer()


def analyzeSentiment(idchat):
    messages = loads(getChat(idchat))
    df = pd.DataFrame(messages)
    polarity = []
    conversation_polarity = 0
    for message in df['text']:
        snt = sid.polarity_scores(message)
        conversation_polarity += snt['compound']
        polarity.append(snt['compound'])
    df['polarity'] = polarity
    df2 = df[["idUser", 'polarity']].groupby(by='idUser', as_index=False).sum()
    return json.dumps({
        'conversation_polarity': conversation_polarity/len(df['text']),
        'users_polarity': df2.to_json(orient='records')
    })


def main():
    analyzeSentiment("0")


if __name__ == '__main__':
    main()
