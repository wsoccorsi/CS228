import numpy as np
import pickle
import os
import re


gestureFile1 = 'userData/train0.dat'
pickle_in = open(gestureFile1, "rb")
gesture_dataN = pickle.load(pickle_in)
print(gesture_dataN.shape)

gestureFile2 = 'userData/train9.dat'
pickle_in = open(gestureFile1, "rb")
gesture_dataM = pickle.load(pickle_in)
print(gesture_dataM.shape)


gestureFile3 = 'userData/train0-2.dat'
pickle_in = open(gestureFile1, "rb")
testN = pickle.load(pickle_in)


gestureFile4 = 'userData/train9-2.dat'
pickle_in = open(gestureFile1, "rb")
testM = pickle.load(pickle_in)

def ReshapeData(set1,set2):
    X = np.zeros((2000,5*4*6),dtype='f')
    Y = np.zeros((2000,5*4*6),dtype='f')
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
# print trainX.shape

