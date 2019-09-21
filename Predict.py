import matplotlib.pyplot as plt
from knn import KNN


print(1)
knn = KNN()
knn.Load_Dataset('data/iris.csv')

x = knn.data[:,0]
y = knn.data[:,1]


trainX = knn.data[::2,0:2]
trainy = knn.target[::2]

#visualization
plt.figure()
plt.scatter(x,y,c=knn.target)
plt.show()
