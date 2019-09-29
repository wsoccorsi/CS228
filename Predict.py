import matplotlib.pyplot as plt
import numpy as np
from knn import KNN


knn = KNN()
knn.Load_Dataset('data/iris.csv')

x = knn.data[:,0]
y = knn.data[:,1]


trainX = knn.data[::2,1:3]
trainy = knn.target[::2]

testX = knn.data[1::2,1:3]
testy = knn.target[1::2]




colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
actualClass = testy[0]
prediction = knn.Predict(testX[0, 0:2])

#visualization
plt.figure()
# plt.scatter(trainX[:,0],trainX[:,1],c=trainy)
# plt.scatter(testX[:,0],testX[:,1],c=testy)

[numItems, numFeatures] = knn.data.shape
for i in range(0, numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    plt.scatter(trainX[i,0], trainX[i,1], facecolor=currColor, edgeColor=[0,0,0], s=50, lw=2)

correct = 0
for i in range(0, numItems/2):
    itemClass = int(testy[i])
    currColor = colors[itemClass, :]
    prediction = int(knn.Predict(testX[i, :]))
    edgeColor = colors[prediction, :]
    if int(prediction) == int(testy[i]):
        correct+=1

    plt.scatter(testX[i,0], testX[i,1], facecolor=currColor, edgecolor=edgeColor, s=50, lw=2)

print((float(correct)/float(numItems/2)) * 100)
plt.show()
