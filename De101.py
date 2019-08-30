import sys
sys.path.insert(0,'..')
import Leap



import pygame
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowDepth, pygameWindowWidth
from random import randint

pw = PYGAME_WINDOW()
x = pygameWindowWidth - pw.screen.get_width() // 2
y = pygameWindowDepth - pw.screen.get_height() // 2
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

def Perturb_Circle_Position():
    fourSidedDieRoll = randint(1,4)
    global x, y
    if fourSidedDieRoll == 1:
        x = x-1
    elif fourSidedDieRoll == 2:
        x = x+1
    elif fourSidedDieRoll == 3:
        y = y-1
    else:
        y = y+1

def Handle_Frame(frame):
     global x, y, xMin, xMax, yMin, yMax
     hand = frame.hands[0]
     fingers = hand.fingers
     indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
     indexFinger = indexFingerList[0]

     distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
     tip = distalPhalanx.next_joint
     x = int(tip[0])
     y = int(tip[1])

     if (x < xMin):
         xMin = x
     if (x > xMax):
         xMax = x
     if (y < yMin):
         yMin = y
     if (y > yMax):
         yMax = y

     print xMin
     print xMax
     print yMin
     print yMax

''' So, create a function that takes five arguments: A value (argument 1) that lies within a range defined
    by arguments 2 and 3 should be scaled such that i now lies within the new range defined by arguments 4 and 5
    returns x or y scaled
    https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio'''
def Scaled(xory, oldMin, oldMax, newMin, newMax): #min, max of original, min max for new scaled
    OldRange = (oldMax - oldMin)
    NewRange = (newMax - newMin)
    if (xory - oldMin) * NewRange != 0:
        NewValue = (((xory - oldMin) * NewRange) / OldRange) + newMin
        return NewValue
    else:
        return 0

controller = Leap.Controller()

while True:
    pw.Prepare()
    frame = controller.frame() #frame grab
    handlist = frame.hands

    if ( len(handlist) > 0):
        Handle_Frame(frame)
        pygameX = Scaled(x, xMin, xMax, 0, pygameWindowWidth)
        pygameY = Scaled(y, yMin, yMax, pygameWindowDepth,0) #my genius inversion tactic

        pw.Draw_Black_Circle(pygameX, pygameY)

    pw.Reveal()
    Perturb_Circle_Position()