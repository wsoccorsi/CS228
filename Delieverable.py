
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowDepth, pygameWindowWidth
from random import randint
import Leap

class DELIVERABLE:

    def __init__(self, pw, x, y, xMin, xMax, yMin, yMax, numberOfHands):
        self.pw = pw
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.controller = Leap.Controller()
        self.numberOfHands = numberOfHands



    def Handle_Bone(self, bone, width):
        base = bone.prev_joint
        print(base)
        tip = bone.next_joint
        xBase, yBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip = self.Handle_Vector_From_Leap(tip)
        self.pw.Draw_Black_Line(xBase, yBase, xTip, yTip, width)

    def Handle_Frame(self):
        frame = self.controller.frame
        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
            for b in range(0, 4):
                self.Handle_Bone(b)

    def Handle_Finger(self, frame):
        hand = frame.hands[0]
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

                self.Handle_Bone(bone, w)


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
            self.Handle_Finger(frame)

        self.pw.Reveal()
        # self.Perturb_Circle_Position()