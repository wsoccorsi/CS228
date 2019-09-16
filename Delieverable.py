
from constants import pygameWindowDepth, pygameWindowWidth
from random import randint
import Leap
import numpy as np
import pickle

class DELIVERABLE:

    def __init__(self, pw, x, y, xMin, xMax, yMin, yMax):
        self.pw = pw
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.controller = Leap.Controller()
        self.currentNumberOfHands = 0
        self.previousNumberOfHands = 0
        self.gestureData = np.zeros((5,4,6), dtype='f')
        self.ending = False



    def Handle_Bone(self, bone, width, h_num):
        base = bone.prev_joint
        tip = bone.next_joint
        xBase, yBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip = self.Handle_Vector_From_Leap(tip)
        if h_num == 1:
            color = 0, 255, 0
        else:
            color = 255, 0, 0

        if self.ending is False:
            for i in range(0, 4):
                for j in range(0, 4):

                    self.gestureData[i,j, 0] = bone.prev_joint[0]
                    self.gestureData[i,j, 1] = bone.prev_joint[1]
                    self.gestureData[i,j, 2] = bone.prev_joint[2]
                    self.gestureData[i,j, 3] = bone.next_joint[0]
                    self.gestureData[i,j, 4] = bone.next_joint[1]
                    self.gestureData[i,j, 5] = bone.next_joint[2]


        self.currentNumberOfHands = h_num

        self.pw.Draw_Line(xBase, yBase, xTip, yTip, width, color)


    def Handle_Finger(self, frame):
        hand = frame.hands[0]
        if len(frame.hands) == 2:
            h_num = 2
        else:
            h_num = 1
        fingers = hand.fingers
        for finger in fingers:
            for b in range(0, 4):
                w = 3
                if b == 0:
                    bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                elif b == 1:
                    bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                elif b == 2:
                    bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
                    # w=2
                elif b == 3:
                    bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                    # w = 1

                self.Handle_Bone(bone, w, h_num)


    def Handle_Vector_From_Leap(self, v):

        self.x, self.y = v[0], v[2]


        if (self.x < self.xMin):
            self.xMin = self.x
        if (self.x > self.xMax):
            self.xMax = self.x
        if (self.y < self.yMin):
            self.yMin = self.y
        if (self.y > self.yMax):
            self.yMax = self.y

        pygameX = self.Scaled(self.x, self.xMin, self.xMax, 0, pygameWindowWidth)
        pygameY = self.Scaled(self.y, self.yMin, self.yMax, 0, pygameWindowDepth)  # my genius inversion tactic
        return pygameX, pygameY

    ''' So, create a function that takes five arguments: A value (argument 1) that lies within a range defined
        by arguments 2 and 3 should be scaled such that i now lies within the new range defined by arguments 4 and 5
        returns x or y scaled
        https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio'''

    def Scaled(self, xory, oldMin, oldMax, newMin, newMax):  # min, max of original, min max for new scaled
        OldRange = (oldMax - oldMin)
        NewRange = (newMax - newMin)
        if (xory - oldMin) * NewRange != 0:
            NewValue = (((xory - oldMin) * NewRange) / OldRange) + newMin
            return NewValue
        else:
            return 0

    controller = Leap.Controller()

    def Run_Forever(self):

        while True:
          self.Run_Once()

    def Run_Once(self):
        self.pw.Prepare()
        frame = self.controller.frame()  # frame grab
        handlist = frame.hands

        if (len(handlist) > 0):
            self.ending = False
            self.Handle_Finger(frame)
        else:
            self.ending = True
            self.Handle_Finger(frame)
            self.Recording_Is_Ending()
            self.Save_Gesture()

        self.pw.Reveal()
        self.previousNumberOfHands = self.currentNumberOfHands

    def Recording_Is_Ending(self):

        print(self.gestureData[0,3,3:6])
        print('recording is ending.')

    def Save_Gesture(self):
        pickle_out = open("userData/gesture", "wb")
        pickle.dump( self.gestureData, pickle_out)
