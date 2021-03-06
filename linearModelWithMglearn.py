import tool
from numpy import *
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB


def testLogistic():
    logreg = LogisticRegression(C=1)
    trainingset, traininglabels = tool.file2floatMatrix('horseColicTraining.txt', 21)
    testset, testlabels = tool.file2floatMatrix('horseColicTest.txt', 21)
    logreg.fit(trainingset, traininglabels)
    print("logreg.coef_: {}".format(logreg.coef_))
    print("logreg.intercept_: {}".format(logreg.intercept_))
    print("Training set score: {:.2f}".format(logreg.score(trainingset, traininglabels)))
    print("Test set score: {:.2f}".format(logreg.score(testset, testlabels)))


def testSVM():
    svc = LinearSVC(C=50)
    trainingset, traininglabels = tool.file2floatMatrix('horseColicTraining.txt', 21)
    testset, testlabels = tool.file2floatMatrix('horseColicTest.txt', 21)
    svc.fit(trainingset, traininglabels)
    print("svc.coef_: {}".format(svc.coef_))
    print("svc.intercept_: {}".format(svc.intercept_))
    print("Training set score: {:.2f}".format(svc.score(trainingset, traininglabels)))
    print("Test set score: {:.2f}".format(svc.score(testset, testlabels)))


if __name__ == '__main__':
    # testSVM()
    testLogistic()
    # testLasso()
    # testOLS()
