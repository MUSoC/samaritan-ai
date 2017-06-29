import feature_vector
import cPickle as pickle
from sklearn import svm
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")


# Create desired output array for SVM
def create_output_desired(sentence_class):
    output_desired = []
    for index in xrange(0, len(sentence_class)):
        output_desired.append(1)
    for index in xrange(0, len(sentence_class)):
        output_desired.append(0)
    return output_desired


# Classification of feature vectors
def classify(feature_vector, output_desired):
    clf = svm.SVC(kernel="linear", C=1, gamma=1)
    # plt.scatter(feature_vector, output_desired)
    # plt.show()
    print clf.fit(feature_vector, output_desired)
    print clf.support_vectors_


def run():
    pos_sentence_class = pickle.load(open("pickledumps/pos_sentence_class.p", "rb")) # noqa
    neg_sentence_class = pickle.load(open("pickledumps/neg_sentence_class.p", "rb")) # noqa

    '''pos_output_desired = create_output_desired(pos_sentence_class)
    neg_output_desired = create_output_desired(neg_sentence_class)'''

    input_feature_vector = feature_vector.run()
    output_desired = create_output_desired(pos_sentence_class)
    classify(input_feature_vector, output_desired)


if __name__ == "__main__":
    run()
