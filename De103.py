import sys
sys.path.insert(0,'..')
from Delieverable import DELIVERABLE
import pygame
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowDepth, pygameWindowWidth

pw = PYGAME_WINDOW()
x = pygameWindowWidth - pw.screen.get_width() // 2
y = pygameWindowDepth - pw.screen.get_height() // 2
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0
numberOfHands = 2

deliverable = DELIVERABLE(pw, x, y, xMin, xMax, yMin, yMax, numberOfHands)
deliverable.Run_Forever()
exit()




