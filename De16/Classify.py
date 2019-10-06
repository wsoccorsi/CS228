
import numpy as np
import pickle
import os
import re
from knn import KNN
import matplotlib.pyplot as plt

#0.872 !!
#0.8755 after reduce data #1
#0.933 after reduce data #2
#0.9825 after center




def ReduceData(X):
    X = np.delete(X, 1, 1)
    X = np.delete(X, 1, 1)
    X = np.delete(X, 1, 2)
    X = np.delete(X, 1, 2)
    X = np.delete(X, 1, 2)
    return X

def CenterData(X):
    allXCoordinates = X[:, :, 0, :]
    meanValue = allXCoordinates.mean()
    X[:, :, 0, :] = allXCoordinates - meanValue

    allYCoordinates = X[:, :, 1, :]
    meanValue = allYCoordinates.mean()
    X[:, :, 1, :] = allYCoordinates - meanValue

    allZCoordinates = X[:, :, 2, :]
    meanValue = allZCoordinates.mean()
    X[:, :, 2, :] = allZCoordinates - meanValue

    return X


gestureFile1 = 'savedData/train0.dat'
pickle_in = open(gestureFile1, "rb")
gesture_dataN = pickle.load(pickle_in)

gestureFile2 = 'savedData/train9.dat'
pickle_in = open(gestureFile2, "rb")
gesture_dataM = pickle.load(pickle_in)


gestureFile3 = 'savedData/test0.dat'
pickle_in = open(gestureFile3, "rb")
testN = pickle.load(pickle_in)
gestureFile4 = 'savedData/test9.dat'
pickle_in = open(gestureFile4, "rb")
testM = pickle.load(pickle_in)

train2 = pickle.load(open('savedData/Apple_test2.p' , 'rb'))
test2 =  pickle.load(open('savedData/Apple_train2.p', 'rb'))

trainM = ReduceData(gesture_dataM)
trainN = ReduceData(gesture_dataN)
testM =  ReduceData(testM)
testN =  ReduceData(testN)

train2 = ReduceData(train2)
test2 = ReduceData(test2)
train2 = CenterData(train2)
test2 = CenterData(test2)

trainM = CenterData(trainM)
trainN = CenterData(trainN)
testM =  CenterData(testM)
testN =  CenterData(testN)

def ReshapeData(set1,set2, set3):
    X = np.zeros((3000,30),dtype='f')
    Y = np.zeros((3000),dtype='f')
    for row in range(0,1000):
        #here
        Y[row] = 9
        Y[row+1000] = 0
        Y[row + 2000] = 2 #de6
        col = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range(0,3):
                    X[row, col] = set1[j, k, m, row] #top 1000
                    X[row+1000, col] = set2[j, k, m, row] #bottom 1000
                    X[row+2000, col] = set3[j, k, m, row] #de6
                    col = col + 1
    return X, Y

trainX, trainY = ReshapeData(trainM, trainN, train2)
testX, testY = ReshapeData(testM, testN, test2)




print trainY.shape
knn = KNN()
knn.Use_K_Of(15)
knn.Fit(trainX, trainY)


print testX.shape
correct_count = 0
for row in range(0, len(trainX)):
    # itemClass = row
    # print(testX[row, :])
    prediction = int(knn.Predict(testX[row, :]))
    print(str(prediction) + " " + str(testY[row]))
    if prediction == testY[row]:
        correct_count += 1

print float(correct_count)/float(len(trainX))


pickle.dump(knn, open('userData/classifier.p','wb'))




