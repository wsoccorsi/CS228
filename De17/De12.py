import sys
sys.path.insert(0,'../..')
import Leap
import time
import Dict


import pygame
import pickle
import numpy as np
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowDepth, pygameWindowWidth
from random import randint
from timeit import default_timer as timer
from random import randrange


# import CenterData
clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros((1,30),dtype='f')
pw = PYGAME_WINDOW()
x = pygameWindowWidth - pw.screen.get_width() // 2
y = pygameWindowDepth - pw.screen.get_height() // 2
number = 0 #run once
lastNumber = number

pauseCheckStart = 0
pauseCheckEnd = 0
correct = False
lastCorrect = False
start = True
userName = ''
database = {}
startTime = timer()
end = 0

xMin =  1000.0
xMax = -1000.0
yMin =  1000.0
yMax = -1000.0



def CenterData(testData):
    allXCoordinates = testData[0,::3]
    meanValue = allXCoordinates.mean()
    testData[0, ::3] = allXCoordinates - meanValue

    allYCoordinates = testData[0,1::3]
    meanValue = allYCoordinates.mean()
    testData[0, 1::3] = allYCoordinates - meanValue

    allZCoordinates = testData[0,2::3]
    meanValue = allZCoordinates.mean()
    testData[0, 2::3] = allZCoordinates - meanValue

    return testData

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
     for finger in fingers:
         for b in range(0, 4):
             Handle_Bone(b)


def Handle_Finger(finger):
    global x, y, xMin, xMax, yMin, yMax, testData, number, correct, database, startTime, lastNumber, end
    hand = frame.hands[0]
    fingers = hand.fingers
    k = 0
    for finger in fingers:
        for b in range(0, 4):
            w = 3
            if b == 0:
                bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
            elif b ==1:
                bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
            elif b == 2:
                bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
                w=2
            elif b ==3:
                bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                w = 1

            tip = bone.next_joint
            xTip, yTip, zTip = tip[0], tip[1], tip[2]
            if ((b == 0) or (b == 3)):
                testData[0, k] = xTip
                testData[0, k + 1] = yTip
                testData[0, k + 2] = zTip
                k = k + 3

            Handle_Bone(bone, w)

    testData = CenterData(testData)
    predictedClass = clf.Predict(testData)
    end = timer()

    if end - startTime > max(10, (15 - database[userName]['digit' + str(number) + 'attempted'])): #if the start time is over 20 then pick a new number
        database = Dict.update_database_time(userName, 'mean' + str(number) + 'time', end-startTime)
        number = randrange(10)

    if predictedClass == number:
        #show check mark
        pw.Prepare()
        image = pygame.image.load('images/iconmonstr-check-mark-1.png')
        pw.screen.blit(image, (pygameWindowWidth/2 + 100, 150))
        pw.Reveal()
        pygame.display.update()

        #correct handle
        correct = True

        #find the time taken to sign
        timeTaken = end - startTime


        #increment the digit signed and start the timer for the next digit
        database = Dict.input_database_sign(userName, 'digit' + str(number) + 'attempted')
        database = Dict.update_database_time(userName, 'mean' + str(number) + 'time', timeTaken)
        startTime = timer()
        lastNumber = number

        #if I've signed this one correct four times get a new number
        if database[userName]['digit' + str(number) + 'attempted'] > 3:
            sorted_dict = sorted(database[userName].items(), key=lambda kv: kv[1])[0] #grab the lowest signed number
            number = int(sorted_dict[0][len('digit'):len('digit')+1])
            lastNumber = number #?

        number = 10 #disable number







def Handle_Bone(bone, width):
    global database
    base = bone.prev_joint
    tip  = bone.next_joint
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)


    pw.Draw_Black_Line(xBase, yBase, xTip, yTip, width)



def Handle_Vector_From_Leap(v):
    global x, y, xMin, xMax, yMin, yMax

    x, y = v[0], v[2]

    if (x < xMin):
        xMin = x
    if (x > xMax):
        xMax = x
    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y

    pygameX = Scaled(x, xMin, xMax, 0, pygameWindowWidth/2)
    pygameY = Scaled(y, yMin, yMax, 0, pygameWindowDepth/2)  # my genius inversion tactic
    return pygameX, pygameY,



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

    #database handle start
    if start:
        userName, database = Dict.init_database()
        sorted_dict = sorted(database[userName].items(), key=lambda kv: kv[1])[0]  # grab the lowest signed number
        number = int(sorted_dict[0][len('digit'):len('digit')+1])

        start = False


    if (len(handlist) > 0):
        Handle_Finger(frame)
        if correct == False:
            if number != 10: #10 is equivalent to a void number
                pw.Adjust_Hand(xBase, yBase, number, database[userName]['digit' + str(number) + 'attempted'],
                               database[userName]['mean'+str(number)+'time'], end - startTime)
                if end - startTime > max(5, 10 - database[userName]['digit' + str(number) + 'attempted']):
                    image = pygame.image.load('images/look_at_the_time.png')
                    pw.screen.blit(image, (pygameWindowWidth / 2 + 200, 0))
    else:
        pw.Put_Hand_Over()

    hand = frame.hands[0]
    finger = hand.fingers[2]
    bone = finger.bone(0)
    base = bone.prev_joint
    xBase, yBase = Handle_Vector_From_Leap(base)




    pw.Reveal()
    Perturb_Circle_Position()
    # pygame.display.update()

    if lastCorrect == True:
        lastCorrect = False
        time.sleep(3)
        startTime = timer()

        number = lastNumber


    if correct:
        lastCorrect = True
        correct = False



