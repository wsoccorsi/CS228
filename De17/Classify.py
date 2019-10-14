
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

train1 = pickle.load(open('savedData/Genovese_test1.p' , 'rb'))
test1 =  pickle.load(open('savedData/Genovese_train1.p', 'rb'))

train3 = pickle.load(open('savedData/Gordon_test3.p' , 'rb'))
test3 =  pickle.load(open('savedData/Gordon_train3.p', 'rb'))

train4 = pickle.load(open('savedData/Deluca_test4.p' , 'rb'))
test4 =  pickle.load(open('savedData/Deluca_train4.p', 'rb'))

train5 = pickle.load(open('savedData/Deluca_test5.p' , 'rb'))
test5 =  pickle.load(open('savedData/Deluca_train5.p', 'rb'))

train6 = pickle.load(open('savedData/test6.dat' , 'rb'))
test6 =  pickle.load(open('savedData/train6.dat', 'rb'))

train7 = pickle.load(open('savedData/test7.dat' , 'rb'))
test7 =  pickle.load(open('savedData/train7.dat', 'rb'))

train8 = pickle.load(open('savedData/Erickson_test8.p' , 'rb'))
test8 =  pickle.load(open('savedData/Erickson_train8.p', 'rb'))



trainM = ReduceData(gesture_dataM)
trainN = ReduceData(gesture_dataN)
testM =  ReduceData(testM)
testN =  ReduceData(testN)

train2 = ReduceData(train2)
test2 = ReduceData(test2)
train2 = CenterData(train2)
test2 = CenterData(test2)


train1 = ReduceData(train1)
test1 = ReduceData(test1)
train1 = CenterData(train1)
test1 = CenterData(test1)

train3 = ReduceData(train3)
test3 = ReduceData(test3)
train3 = CenterData(train3)
test3 = CenterData(test3)

train4 = ReduceData(train4)
test4 = ReduceData(test4)
train4 = CenterData(train4)
test4 = CenterData(test4)

train5 = ReduceData(train5)
test5 = ReduceData(test5)
train5 = CenterData(train5)
test5 = CenterData(test5)

train6 = ReduceData(train6)
test6 = ReduceData(test6)
train6 = CenterData(train6)
test6 = CenterData(test6)

train7 = ReduceData(train7)
test7 = ReduceData(test7)
train7 = CenterData(train7)
test7 = CenterData(test7)

train8 = ReduceData(train8)
test8 = ReduceData(test8)
train8 = CenterData(train8)
test8 = CenterData(test8)

trainM = CenterData(trainM)
trainN = CenterData(trainN)
testM =  CenterData(testM)
testN =  CenterData(testN)

def ReshapeData(set1,set2, set3, set4, set5, set6, set7, set8, set9, set10):
    X = np.zeros((10000,30),dtype='f')
    Y = np.zeros((10000),dtype='f')
    for row in range(0,1000):
        #here
        Y[row] = 9
        Y[row+1000] = 0
        Y[row + 2000] = 2
        Y[row + 3000] = 1
        Y[row + 4000] = 3
        Y[row + 5000] = 4
        Y[row + 6000] = 5
        Y[row + 7000] = 6
        Y[row + 8000] = 7
        Y[row + 9000] = 8

        col = 0
        for j in range(0,5):
            for k in range(0,2):
                for m in range(0,3):
                    X[row, col] = set1[j, k, m, row] #top 1000
                    X[row+1000, col] = set2[j, k, m, row] #bottom 1000
                    X[row+2000, col] = set3[j, k, m, row] #de6
                    X[row+3000, col] = set4[j, k, m, row] #de6
                    X[row+4000, col] = set5[j, k, m, row] #de6
                    X[row+5000, col] = set6[j, k, m, row] #de6
                    X[row+6000, col] = set7[j, k, m, row] #de6
                    X[row+7000, col] = set8[j, k, m, row] #de6
                    X[row+8000, col] = set9[j, k, m, row] #de6
                    X[row+9000, col] = set10[j, k, m, row] #de6

                    col = col + 1
    return X, Y

trainX, trainY = ReshapeData(trainM, trainN, train2, train1, train3, train4, train5, train6, train7, train8)
testX, testY = ReshapeData(testM, testN, test2, test1, test3, test4, test5, test6, test7, test8)




print trainY.shape
knn = KNN()
knn.Use_K_Of(15)
knn.Fit(trainX, trainY)


print testX.shape
correct_count = 0
count = 1
for row in range(0, len(trainX)):
    # itemClass = row
    # print(testX[row, :])==
    prediction = int(knn.Predict(testX[row, :]))
    print(str(prediction) + " " + str(testY[row]) + ' ' + str(float(count)))
    count +=1
    if prediction == testY[row]:
        correct_count += 1

print float(correct_count)/float(len(trainX))


pickle.dump(knn, open('userData/classifier.p','wb'))




