import  pickle
import  numpy
import os
import re
from constants import pygameWindowDepth, pygameWindowWidth
import time
import shutil

class READER:

    def __init__(self, pw):
        self.numGestures = 0
        self.pygameWindow = pw
        self.xMin = 1000.0
        self.xMax = -1000.0
        self.yMin = 1000.0
        self.yMax = -1000.0
        self.x = pygameWindowWidth - pw.screen.get_width() // 2
        self.y = pygameWindowDepth - pw.screen.get_height() // 2



    def Number_Of_Gestures(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)

    def Restart_Directory(self):
        shutil.rmtree('userData')
        os.mkdir('userData')

    def Print_Gestures(self):
        gestureFile = 'userData/gesture0'
        while os.path.exists(gestureFile):
            pickle_in = open(gestureFile, "rb")
            gesture_data = pickle.load(pickle_in)

            iteration = int(re.search(r'\d+', gestureFile).group())
            iteration = iteration + 1
            gestureFile = "userData/gesture" + str(iteration)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()

    def Draw_Each_Gesture_Once(self):
        gestureFile = 'userData/gesture0'

        while os.path.exists(gestureFile):
            self.pygameWindow.Prepare()
            iteration = int(re.search(r'\d+', gestureFile).group())
            self.Draw_Gesture(iteration)
            self.pygameWindow.Reveal()
            iteration = iteration + 1
            gestureFile = "userData/gesture" + str(iteration)


    def Draw_Gesture(self, gestNum):
        gestureFile = 'userData/gesture' + str(gestNum)
        pickle_in = open(gestureFile, "rb")
        gesture_data = pickle.load(pickle_in)
        for i in range (0, 5):
            for j in range(0, 4):
                xBaseNotYetScaled = gesture_data[i,j,0]
                yBaseNotYetScaled = gesture_data[i,j,2]
                xTipNotYetScaled = gesture_data[i,j,3]
                yTipNotYetScaled = gesture_data[i,j,5]

                # if (xBaseNotYetScaled < self.xMin):
                #     self.xMin = xBaseNotYetScaled
                # if (xBaseNotYetScaled > self.xMax):
                #     self.xMax = xBaseNotYetScaled
                # if (yBaseNotYetScaled < self.yMin):
                #     self.yMin = yBaseNotYetScal ed
                # if (yBaseNotYetScaled > self.yMax):
                #     self.yMax = yBaseNotYetScaled



                xBase = self.Scaled(xBaseNotYetScaled, self.xMin, self.xMax, pygameWindowWidth, 0)
                yBase = self.Scaled(yBaseNotYetScaled, self.yMin, self.yMax, pygameWindowDepth, 0)


                # if (xTipNotYetScaled < self.xMin):
                #     self.xMin = xTipNotYetScaled
                # if (xTipNotYetScaled > self.xMax):
                #     self.xMax = xTipNotYetScaled
                # if (yTipNotYetScaled < self.yMin):
                #     self.yMin = yTipNotYetScaled
                # if (yTipNotYetScaled > self.yMax):
                #     self.yMax = yTipNotYetScaled
                xTip = self.Scaled(xTipNotYetScaled, self.xMin, self.xMax, pygameWindowWidth, 0)
                yTip = self.Scaled(yTipNotYetScaled, self.yMin, self.yMax, pygameWindowDepth, 0)

                self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, 1, (0, 0, 255))
                time.sleep(0.1)



    def Scaled(self, xory, oldMin, oldMax, newMin, newMax): #min, max of original, min max for new scaled
        OldRange = (oldMax - oldMin)
        NewRange = (newMax - newMin)
        if (xory - oldMin) * NewRange != 0:
            NewValue = (((xory - oldMin) * NewRange) / OldRange) + newMin
            return NewValue
        else:
            return 0