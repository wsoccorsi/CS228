import pygame
from constants import pygameWindowWidth, pygameWindowDepth

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((pygameWindowWidth,pygameWindowDepth))

    def Prepare(self):
        pygame.event.get()
        self.bg_color = 255, 255, 255
        self.screen.fill(self.bg_color)

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self, x, y):
        black = 0,0,0
        # https://stackoverflow.com/questions/40953796/getting-the-center-of-surfaces-in-pygame-with-python-3-4
        pygame.draw.circle(self.screen, black, (x, y), 25)

    def Draw_Line(self, xBase, yBase, xTip, yTip, width, color):
        pygame.draw.line(self.screen, color, (xBase, yBase), (xTip, yTip), width)
