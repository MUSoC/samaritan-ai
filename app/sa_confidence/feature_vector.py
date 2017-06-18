# import preprocess
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer


# Calculating tfidf
def calculate_tfidf(list_data):
    vectorizer.fit_transform(list_data)
    idf = vectorizer.idf_
    return dict(zip(vectorizer.get_feature_names(), idf))


def run():
    paras_pos_single = pickle.load(open("pickledumps/paras_pos_single.p", "rb")) # noqa
    paras_neg_single = pickle.load(open("pickledumps/paras_neg_single.p", "rb")) # noqa
    # print paras_pos_single, '\n-------------\n', paras_neg_single
    pos_tfidf = calculate_tfidf(paras_pos_single)
    neg_tfidf = calculate_tfidf(paras_neg_single)
    print pos_tfidf, '\n-------------\n', neg_tfidf


vectorizer = TfidfVectorizer(min_df=1)

if __name__ == "__main__":
    run()
