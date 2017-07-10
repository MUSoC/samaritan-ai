import preprocess
import nltk
import cPickle as pickle


# Assign pos tags to words
def assign_POS_tags(paras_pos):
    para_data = []
    for para in paras_pos:
        pos_data = []
        for sentence in para:
            pos_data.append(nltk.pos_tag(sentence.split()))
        para_data.append(pos_data)
    return para_data


# Assign features for POS
def assign_feature_POS(data_POS):
    # Checking for adverds, verbs and adjectives
    check_list = ['JJ', 'RB', 'VB', 'VBD']
    feature_POS = []
    for paragraph in data_POS:
        POS_number = 0
        sentence_len = 1
        for sentence in paragraph:
            for word in sentence:
                if word[1] in check_list:
                    POS_number += 1
        feature_POS.append(POS_number/len(paragraph))
    return feature_POS


def run():
    file_type, paras_pos, paras_neg = preprocess.run()
    pos_data_POS = assign_POS_tags(paras_pos)
    neg_data_POS = assign_POS_tags(paras_neg)

    pos_feature_POS = assign_feature_POS(pos_data_POS)
    neg_feature_POS = assign_feature_POS(neg_data_POS)

    # Creating dump files of positive and negative pos tagged words
    if file_type == 1:
        pickle.dump(pos_data_POS, open("pickledumps/train/pos_POS_TAGGED.p", "wb"))
        pickle.dump(neg_data_POS, open("pickledumps/train/neg_POS_TAGGED.p", "wb"))
    else:
        pickle.dump(pos_data_POS, open("pickledumps/test/pos_POS_TAGGED.p", "wb"))
        pickle.dump(neg_data_POS, open("pickledumps/test/neg_POS_TAGGED.p", "wb"))

    # Creating dump files of the pos and neg feature vectors for POS tagged
    if file_type == 1:
        pickle.dump(pos_feature_POS, open("pickledumps/train/pos_feature_POS.p", "wb"))
        pickle.dump(neg_feature_POS, open("pickledumps/train/neg_feature_POS.p", "wb"))
    else:
        pickle.dump(pos_feature_POS, open("pickledumps/test/pos_feature_POS.p", "wb"))
        pickle.dump(neg_feature_POS, open("pickledumps/test/neg_feature_POS.p", "wb"))

    return paras_pos, paras_neg


if __name__ == "__main__":
    run()
