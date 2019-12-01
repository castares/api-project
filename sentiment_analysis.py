from nltk.sentiment.vader import SentimentIntensityAnalyzer
import mongodb as mdb  # This project file mongodb.py
from bson.json_util import loads, dumps
import pandas as pd

sid = SentimentIntensityAnalyzer()


def analyzeSentiment(idchat):
    messages = loads(mdb.getChat(idchat))
    df = pd.DataFrame(messages)
    polarity = []
    conversation_polarity = 0
    for message in df['text']:
        snt = sid.polarity_scores(message)
        conversation_polarity += snt['compound']
        polarity.append(snt['compound'])
    df['polarity'] = polarity
    df.groupby('users').agg(['polarity']).sum()
    print(f'conversation_polarity: {conversation_polarity}')
    print(df)
    return


def main():
    analyzeSentiment("0")


if __name__ == '__main__':
    main()
