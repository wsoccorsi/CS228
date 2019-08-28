import pygame
from pygameWindow import PYGAME_WINDOW
from constants import pygameWindowDepth, pygameWindowWidth
pw = PYGAME_WINDOW()
print(pw)
while True:
    pw.Prepare()
    pw.Draw_Black_Circle(pygameWindowWidth, pygameWindowDepth)
    pw.Reveal()