import preprocess
# import cPickle as pickle


# Calculating score
def calculate_scores(full_text, scores):
    not_removal_list = ['not', 'but', 'if', 'until',
                        'against', 'most', 'no', 'nor', 'very', 'musn\'',
                        'needn\'', 'shan\'', 'shouldn\'', 'wasn\'', 'weren\'',
                        'won\'', 'wouldn\'']
    para_scores = []
    position_data_sentence = []
    position_data_para = []
    prev_word = ''
    for paragraph in full_text:
        score = 0
        word_pos_para = 0
        position_in_sentence = []
        position_in_para = []
        for sentence in paragraph:
            position_sentence = []
            position_para = []
            word_pos = 0
            for word in sentence.split():
                # Calculating word distance from sentence and paragraph
                word_pos += 1
                word_pos_para += 1
                position = (word, word_pos)
                position_paragraph = (word, word_pos_para)
                position_sentence.append(position)
                position_para.append(position_paragraph)
                # Comparing word in paragraph with lexicon
                if word in scores.keys():
                    if prev_word in not_removal_list:
                        scores[word] = scores[word] * -1
                    score += scores[word]
                prev_word = word
            position_in_sentence.append(position_sentence)
            position_in_para.append(position_para)
        position_data_sentence.append(position_in_sentence)
        position_data_para.append(position_in_para)
        para_scores.append(score)
    return para_scores, position_data_sentence, position_data_para


# Creates a sentiment dictionary in the form {word : value}
def create_sentiment_dict(sentimentData):
    afinnfile = open(sentimentData)
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = float(score)
    return scores


def run():
    paras_pos, paras_neg = preprocess.run()
    scores = create_sentiment_dict('lexicon/AFINN-111.txt')
    # scores = create_sentiment_dict('lexicon/wordwithStrength.txt')
    pos_para_score, pos_word_position_sentence, pos_word_position_para = calculate_scores(paras_pos, scores) # noqa
    neg_para_score, neg_word_position_sentence, neg_word_position_para = calculate_scores(paras_neg, scores) # noqa
    # print pos_para_score, '\n-------------\n', neg_para_score
    return paras_pos, paras_neg


if __name__ == "__main__":
    run()
