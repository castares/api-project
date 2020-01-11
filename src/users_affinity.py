from sklearn.metrics.pairwise import euclidean_distances as distance
import nltk
from nltk.corpus import stopwords
from .mongodb import allMessages  # This project file mongodb.py
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def processMessages(messages):
    user_messages = dict()
    for message in messages:
        user_messages.setdefault(message['idUser'], []).append(message['text'])
    for key, value in user_messages.items():
        user_messages[key] = " ".join(value)
    return user_messages


def similarityMatrix(users_messages):
    count_vectorizer = CountVectorizer(stop_words="english")
    sparse_matrix = count_vectorizer.fit_transform(users_messages.values())
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix,
                      columns=count_vectorizer.get_feature_names(),
                      index=users_messages.keys())
    # from sklearn.metrics.pairwise import cosine_similarity as distance
    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(
        similarity_matrix, columns=users_messages.keys(), index=users_messages.keys())
    return sim_df


def similarUsers(iduser):
    sim_df = similarityMatrix(processMessages(allMessages()))
    # Remove diagonal max values and set those to 0
    np.fill_diagonal(sim_df.values, 0)
    return json.dumps({
        iduser: {
            'recommended_users': [e for e in list(
                sim_df[iduser].sort_values(ascending=False)[0:3].index)]
        }
    })


def main():
    mostSimilarUser(0)


if __name__ == '__main__':
    main()
