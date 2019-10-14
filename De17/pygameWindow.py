import pygame
from constants import pygameWindowWidth, pygameWindowDepth
from random import random
from pygame.math import Vector2
from random import randrange


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

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, width):
        black = 0, 0, 0
        pygame.draw.line(self.screen, black, (xBase, yBase), (xTip, yTip), width)

    def Adjust_Hand(self, x, y, number):
        BLUE = pygame.Color('dodgerblue1')
        FONT = pygame.font.Font(None, 250)
        global fresh
        if x < 250:
            image =  pygame.image.load('images/move_right.jpg')
        elif x > 450:
            image =  pygame.image.load('images/move_left.jpg')
        elif y < 100:
            image =  pygame.image.load('images/move_back.jpg')
        elif y > 300:
            image = pygame.image.load('images/move_forward.jpg')
        else: #if centered
            image = pygame.image.load('images/nothing.png')
            self.screen.blit(image, (pygameWindowWidth / 2 , 0))

            image = FONT.render(str(number), True,BLUE)
            self.screen.blit(image, (pygameWindowWidth / 2 + 150, pygameWindowDepth/2))
            return 1

        self.screen.blit(image, (pygameWindowWidth / 2, 0))

        return 0
    def Put_Hand_Over(self):
        image = pygame.image.load('images/hand_over.png')
        self.screen.blit(image, (pygameWindowWidth / 2, 0))