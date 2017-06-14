import pos_tags
# import cPickle as pickle


# Calculating score
def calculate_scores(full_text, scores):
    para_scores = []
    for paragraph in full_text:
        score = 0
        for sentence in paragraph:
            for word in sentence.split():
                # Comparing word in paragraph with lexicon
                if word in scores.keys():
                    # print word, scores[word]
                    score += scores[word]
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
    pos_data_POS, neg_data_POS = pos_tags.run()
    scores = create_sentiment_dict('lexicon/AFINN-111.txt')
    # scores = create_sentiment_dict('lexicon/wordwithStrength.txt')
    pos_para_score = calculate_scores(pos_data_POS, scores)
    neg_para_score = calculate_scores(neg_data_POS, scores)
    print pos_para_score, neg_para_score


if __name__ == "__main__":
    run()
