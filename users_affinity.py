from sklearn.metrics.pairwise import euclidean_distances as distance
import nltk
from nltk.corpus import stopwords
import mongodb as mdb  # This project file mongodb.py
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


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
    return sim_df.idxmax()


def mostSimilarUser(iduser):
    df = similarityMatrix(processMessages(mdb.allMessages()))
    return json.dumps({iduser: str(df.loc[iduser])})


def main():
    mostSimilarUser(0)


if __name__ == '__main__':
    main()
