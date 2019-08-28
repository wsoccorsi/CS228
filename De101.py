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

while True:
    pw.Prepare()
    pw.Draw_Black_Circle(x, y)
    pw.Reveal()
    Perturb_Circle_Position()