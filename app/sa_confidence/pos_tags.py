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


def run():
    paras_pos, paras_neg = preprocess.run()
    pos_data_POS = assign_POS_tags(paras_pos)
    neg_data_POS = assign_POS_tags(paras_neg)

    # Creating dump files of positive and negative pos tagged words
    pickle.dump(pos_data_POS, open("pickledumps/pos_POS_TAGGED.p", "wb"))
    pickle.dump(neg_data_POS, open("pickledumps/neg_POS_TAGGED.p", "wb"))

    return paras_pos, paras_neg


if __name__ == "__main__":
    run()
