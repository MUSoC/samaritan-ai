import glob
import nltk
import re
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Clean sentence
def clean_sentence(sentence):
    # Removing all special characters
    cleaned_sentence = re.sub("[^a-zA-Z\s0-9\-]", "", sentence)
    no_stopwords_sentence = remove_stopwords(cleaned_sentence)
    lemmatized_sentence = lemmatize_sentence(no_stopwords_sentence)
    return lemmatized_sentence


# Remove stopwords
def remove_stopwords(cleaned_sentence):
    stop_words = stopwords.words('english')
    not_removal_list = ['not', 'but', 'if', 'until',
                        'against', 'most', 'no', 'nor', 'very', 'musn\'',
                        'needn\'', 'shan\'', 'shouldn\'', 'wasn\'', 'weren\'',
                        'won\'', 'wouldn\'']
    new_stop_words = []
    for word in stop_words:
        if word not in not_removal_list:
            new_stop_words.append(word)

    no_stopwords_sentence = []
    for sentence in cleaned_sentence.split():
        if sentence not in new_stop_words:
            no_stopwords_sentence.append(sentence)
    return no_stopwords_sentence


# Lemmatize the sentences
def lemmatize_sentence(cleaned_sentence):
    lists = []
    for word in cleaned_sentence:
        lists.append(wordnet_lemmatizer.lemmatize(word))
    return " ".join(lists)


# Create list of sentences
def create_sentences(paragraph):
    sentences = tokenizer.tokenize(paragraph)
    # print sentences
    # Make a list of sentences
    list_sentences = []
    for sentence in sentences:
        if len(sentence) > 0:
            # Converting to lower case and appending it to a list
            list_sentences.append(clean_sentence(sentence.lower()))
    return list_sentences


# Read input files
def get_input_file(filename):
    with open(filename, "r") as file:
        sentences = create_sentences(file.read())
    file.close()
    return sentences


def run():
    pos_filenames = sorted(glob.glob("imdb/pos/*.txt"))
    paras_pos = []
    for pos_filename in pos_filenames:
        # print '\n-----------------------', pos_filename, '---------------------\n' # noqa
        paras_pos.append(get_input_file(pos_filename))

    neg_filenames = sorted(glob.glob("imdb/neg/*.txt"))
    paras_neg = []
    for neg_filename in neg_filenames:
        # print '\n-----------------------', neg_filename, '---------------------\n' # noqa
        paras_neg.append(get_input_file(neg_filename))
    return paras_pos, paras_neg


# Set default encoding as utf-8
reload(sys)
sys.setdefaultencoding('utf8')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
wordnet_lemmatizer = WordNetLemmatizer()

if __name__ == "__main__":
    run()
