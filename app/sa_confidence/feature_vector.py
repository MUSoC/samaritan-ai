import scores
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


# Generate feature vector to give to SVM
def make_feature_vector(tfidf_score, sentence_class, position_score, para_score, feature_POS):
    '''for i in pos_sentence_class:
        print i.filename'''
    feature_vector = []
    for index in xrange(0, len(sentence_class)):
        para_feature = []
        para_feature.append(tfidf_score[index])
        para_feature.append(sentence_class[index].file_rating)
        para_feature.append(position_score[index])
        para_feature.append(para_score[index])
        para_feature.append(feature_POS[index])
        feature_vector.append(para_feature)

    return feature_vector


# Combining feature vectors into one
def combined_feature_vector(pos_feature_vector, neg_feature_vector):
    feature_vector = []
    for vector in pos_feature_vector:
        feature_vector.append(vector)
    for vector in neg_feature_vector:
        feature_vector.append(vector)
    return feature_vector


def run():
    file_type, paras_pos, pos_position_score, pos_para_score, paras_neg, neg_position_score, neg_para_score = scores.run() # noqa

    if file_type == 1:
        paras_pos_single = pickle.load(open("pickledumps/train/paras_pos_single.p", "rb")) # noqa
        paras_neg_single = pickle.load(open("pickledumps/train/paras_neg_single.p", "rb")) # noqa

        pos_sentence_class = pickle.load(open("pickledumps/train/pos_sentence_class.p", "rb")) # noqa
        neg_sentence_class = pickle.load(open("pickledumps/train/neg_sentence_class.p", "rb")) # noqa

        pos_feature_POS = pickle.load(open("pickledumps/train/pos_feature_POS.p", "rb")) # noqa
        neg_feature_POS = pickle.load(open("pickledumps/train/neg_feature_POS.p", "rb")) # noqa
    else:
        paras_pos_single = pickle.load(open("pickledumps/test/paras_pos_single.p", "rb")) # noqa
        paras_neg_single = pickle.load(open("pickledumps/test/paras_neg_single.p", "rb")) # noqa

        pos_sentence_class = pickle.load(open("pickledumps/test/pos_sentence_class.p", "rb")) # noqa
        neg_sentence_class = pickle.load(open("pickledumps/test/neg_sentence_class.p", "rb")) # noqa

        pos_feature_POS = pickle.load(open("pickledumps/test/pos_feature_POS.p", "rb")) # noqa
        neg_feature_POS = pickle.load(open("pickledumps/test/neg_feature_POS.p", "rb")) # noqa
    
    pos_tfidf = calculate_tfidf(paras_pos_single)
    neg_tfidf = calculate_tfidf(paras_neg_single)

    pos_tfidf_score = tfidf_score_paragraphs(paras_pos, pos_tfidf)
    neg_tfidf_score = tfidf_score_paragraphs(paras_neg, neg_tfidf)

    pos_feature_vector = make_feature_vector(pos_tfidf_score, pos_sentence_class, pos_position_score, pos_para_score, pos_feature_POS)
    neg_feature_vector = make_feature_vector(neg_tfidf_score, neg_sentence_class, neg_position_score, neg_para_score, neg_feature_POS)

    feature_vector = combined_feature_vector(pos_feature_vector, neg_feature_vector)

    return file_type, feature_vector


vectorizer = TfidfVectorizer(min_df=1, analyzer='word')

if __name__ == "__main__":
    run()
