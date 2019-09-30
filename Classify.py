import numpy as np
import pickle
import os
import re
from knn import KNN
import matplotlib.pyplot as plt

#0.872 !!



def ReduceData(self, x):
    return x

gestureFile1 = 'savedData/train0.dat'
pickle_in = open(gestureFile1, "rb")
gesture_dataN = pickle.load(pickle_in)
print(gesture_dataN.shape)


gestureFile2 = 'savedData/train9.dat'
pickle_in = open(gestureFile2, "rb")
gesture_dataM = pickle.load(pickle_in)
print(gesture_dataM.shape)


gestureFile3 = 'savedData/train0-2.dat'
pickle_in = open(gestureFile3, "rb")
testN = pickle.load(pickle_in)
gestureFile4 = 'savedData/train9-2.dat'
pickle_in = open(gestureFile4, "rb")
testM = pickle.load(pickle_in)

def ReshapeData(set1,set2):
    X = np.zeros((2000,5*4*6),dtype='f')
    Y = np.zeros((2000),dtype='f')
    for row in range(0,1000):
        #here
        Y[row] = 9
        Y[row+1000] = 0
        col = 0
        for j in range(0,5):
            for k in range(0,4):
                for m in range(0,6):
                    X[row, col] = set1[j, k, m, row] #top 1000
                    X[row+1000, col] = set2[j, k, m, row] #bottom 1000
                    col = col + 1
    return X, Y

trainX, trainY = ReshapeData(gesture_dataM, gesture_dataN)
testX, testY = ReshapeData(testM, testN)


print trainX
print trainY
print testX
print testY

trainM = ReduceData(trainX)
trainN = ReduceData(trainY)
testM =  ReduceData(testM)
testN =  ReduceData(testN)

print trainY.shape
knn = KNN()
knn.Use_K_Of(15)
knn.Fit(trainX, trainY)


print testX.shape
correct_count = 0
for row in range(0, len(trainX)):
    # itemClass = row
    prediction = int(knn.Predict(testX[row, :]))
    print(str(prediction) + " " + str(testY[row]))
    if prediction == testY[row]:
        correct_count += 1

print float(correct_count)/float(len(trainX))








