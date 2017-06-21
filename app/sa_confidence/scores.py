import preprocess
# import cPickle as pickle


# Calculating score
def calculate_scores(full_text, scores):
    not_removal_list = ['not', 'but', 'if', 'until',
                        'against', 'most', 'no', 'nor', 'very', 'musn\'',
                        'needn\'', 'shan\'', 'shouldn\'', 'wasn\'', 'weren\'',
                        'won\'', 'wouldn\'']
    para_scores = []
    prev_word = ''
    for paragraph in full_text:
        score = 0
        for sentence in paragraph:
            for word in sentence.split():
                # Comparing word in paragraph with lexicon
                if word in scores.keys():
                    if prev_word in not_removal_list:
                        scores[word] = scores[word] * -1
                    score += scores[word]
                prev_word = word
        # print '-------------------------'
        para_scores.append(score)
    return para_scores


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
    pos_para_score = calculate_scores(paras_pos, scores)
    neg_para_score = calculate_scores(paras_neg, scores)
    print pos_para_score, '\n-------------\n', neg_para_score
    return paras_pos, paras_neg


if __name__ == "__main__":
    run()
