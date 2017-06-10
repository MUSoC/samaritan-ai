import preprocess
import nltk


# Assign pos tags to words
def assign_POS_tags(paras_pos):
    pos_data = []
    for para in paras_pos:
        for sentence in para:
            pos_data.append(nltk.pos_tag(sentence.split()))
    return pos_data


def run():
    paras_pos, paras_neg = preprocess.run()
    pos_data_POS = assign_POS_tags(paras_pos)
    neg_data_POS = assign_POS_tags(paras_neg)
    print pos_data_POS


if __name__ == "__main__":
    run()
