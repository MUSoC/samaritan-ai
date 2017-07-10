import feature_vector
import cPickle as pickle
import numpy as np
import math
from sklearn import svm


# Create desired output array for SVM
def create_output_desired(sentence_class):
    output_desired = []
    for index in xrange(0, len(sentence_class)):
        output_desired.append(1)
    for index in xrange(0, len(sentence_class)):
        output_desired.append(0)
    return output_desired


# Calculating standard deviation of the feature vector
def calculate_standard_deviation(yy):
    mean_value = np.mean(yy)
    number_files = len(yy)
    sum_of_yy = 0
    for y in yy:
        sum_of_yy = sum_of_yy + ((y - mean_value) * (y - mean_value))
    std = math.sqrt(sum_of_yy / number_files)
    return std


# Classification of feature vectors
def classify(file_type, feature_vector, output_desired):
    if file_type == 1:
        classifier = svm.SVC(kernel="linear", C=1, gamma=1)
        classifier.fit(feature_vector, output_desired)
        pickle.dump(classifier, open("pickledumps/classifier.p", "wb")) # noqa
    else:
        classifier = pickle.load(open("pickledumps/classifier.p", "rb")) # noqa
        classifier.predict(feature_vector)

    w = classifier.coef_[0]
    a = -w[0] / w[1]
    min_value_list = []
    max_value_list = []
    for features in feature_vector:
        min_value_list.append(min(features))
        max_value_list.append(max(features))
    min_value = min(min_value_list)
    max_value = max(max_value_list)
    xx = np.linspace(min_value, max_value)
    yy = a * xx - ((classifier.intercept_[0]) / w[1])
    std = calculate_standard_deviation(yy)
    '''b = classifier.support_vectors_[0]
    yydown = a * xx + (b[1] - a * b[0])
    b = classifier.support_vectors_[-1]
    yyup = a * xx + (b[1] - a * b[0])'''

    # print yydown, '\n--\n', yyup
    # print classifier.support_vectors_


def run():
    file_type, input_feature_vector = feature_vector.run()

    if file_type == 1:
        pos_sentence_class = pickle.load(open("pickledumps/train/pos_sentence_class.p", "rb")) # noqa
        neg_sentence_class = pickle.load(open("pickledumps/train/neg_sentence_class.p", "rb")) # noqa
        output_desired = create_output_desired(pos_sentence_class)
        classify(file_type, input_feature_vector, output_desired)
    else:
        pos_sentence_class = pickle.load(open("pickledumps/test/pos_sentence_class.p", "rb")) # noqa
        neg_sentence_class = pickle.load(open("pickledumps/test/neg_sentence_class.p", "rb")) # noqa
        # output_desired = create_output_desired(pos_sentence_class)
        classify(file_type, input_feature_vector, output_desired=None)


if __name__ == "__main__":
    run()
