import preprocess
import cPickle as pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer


# Calculating tfidf
def calculate_tfidf(list_data):
    vectorizer.fit_transform(list_data)
    idf = vectorizer.idf_
    return dict(zip(vectorizer.get_feature_names(), idf))


# Assigning tfidf score to paragraph
def tfidf_score_paragraphs(full_text, tfidf):
    para_scores_tfidf = []
    for paragraph in full_text:
        score = 0
        n_words = 0
        for sentence in paragraph:
            # n_words = len(sentence)
            for word in sentence.split():
                if re.match("[a-zA-Z]", word):
                    n_words += 1
                    # Comparing word in paragraph with tfidf dict
                    try:
                        score += tfidf[word]
                    except:
                        score += 0
                        pass
        # print '-------------------------'
        tfidf_score = float(score) / n_words
        para_scores_tfidf.append(tfidf_score)
    return para_scores_tfidf


def run():
    paras_pos_single = pickle.load(open("pickledumps/paras_pos_single.p", "rb")) # noqa
    paras_neg_single = pickle.load(open("pickledumps/paras_neg_single.p", "rb")) # noqa
    paras_pos, paras_neg = preprocess.run()
    # print paras_pos
    # print paras_pos_single, '\n-------------\n', paras_neg_single
    '''pos_tfidf = calculate_tfidf(paras_pos_single)
    neg_tfidf = calculate_tfidf(paras_neg_single)
    pos_tfidf_score = tfidf_score_paragraphs(paras_pos, pos_tfidf)
    neg_tfidf_score = tfidf_score_paragraphs(paras_neg, neg_tfidf)'''


vectorizer = TfidfVectorizer(min_df=1, analyzer='word')

if __name__ == "__main__":
    run()
