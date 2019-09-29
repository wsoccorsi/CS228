import numpy as np
import pickle
import os
import re


gestureFile = 'userData/gesture0'


while os.path.exists(gestureFile):
    pickle_in = open(gestureFile, "rb")
    gesture_data = pickle.load(pickle_in)
    iteration = int(re.search(r'\d+', gestureFile).group())
    iteration = iteration + 1
    gestureFile = "userData/gesture" + str(iteration)
    print(gesture_data.shape)