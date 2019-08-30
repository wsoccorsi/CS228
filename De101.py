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
     global x, y
     hand = frame.hands[0]
     fingers = hand.fingers
     indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
     indexFinger = indexFingerList[0]

     distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
     tip = distalPhalanx.next_joint
     x = int(tip[0])
     y = int(tip[1])



controller = Leap.Controller()

while True:
    pw.Prepare()
    frame = controller.frame() #frame grab
    handlist = frame.hands
    print("before")
    print(x)
    if ( len(handlist) > 0):
        Handle_Frame(frame)
    print("after")
    print(y)
    pw.Draw_Black_Circle(x, y)
    pw.Reveal()
    Perturb_Circle_Position()