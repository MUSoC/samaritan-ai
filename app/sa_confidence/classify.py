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
def classify(file_type, feature_vector, output_desired):
    if file_type == 1:
        classifier = svm.SVC(kernel="linear", C=1, gamma=1)
        # plt.scatter(feature_vector, output_desired)
        # plt.show()
        classifier.fit(feature_vector, output_desired)
        pickle.dump(classifier, open("pickledumps/classifier.p", "wb")) # noqa
    else:
        classifier = pickle.load(open("pickledumps/classifier.p", "rb")) # noqa
        print classifier.predict(feature_vector)

        # print classifier


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
        classify(file_type, input_feature_vector, output_desired=None)

        


if __name__ == "__main__":
    run()
