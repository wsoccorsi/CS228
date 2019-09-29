import sys
sys.path.insert(0,'..')
from Recorder import RECORDER
import pygame
from pygameWindow_De103 import PYGAME_WINDOW
from constants import pygameWindowDepth, pygameWindowWidth
from Reader import READER

pw = PYGAME_WINDOW()
x = pygameWindowWidth - pw.screen.get_width() // 2
y = pygameWindowDepth - pw.screen.get_height() // 2
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

reader = READER(pw)
reader.Restart_Directory()
deliverable = RECORDER(pw, x, y, xMin, xMax, yMin, yMax)
deliverable.Run_Forever()
exit()




