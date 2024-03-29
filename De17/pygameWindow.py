import pygame
from constants import pygameWindowWidth, pygameWindowDepth
from random import random
from pygame.math import Vector2
from random import randrange
import math


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

    def Adjust_Hand(self, x, y, number, attempts, avgTime, currentTime, topTimeSigned, basicNum1, basicNum2, type, correctSigns):
        BLUE = pygame.Color('dodgerblue1')
        FONT2 = pygame.font.Font(None, 100)
        FONT3 = pygame.font.Font(None, 40)

        if number != 10:
            sorted_times = sorted(topTimeSigned[str(number)].items(), key=lambda kv: kv[1])  # grab the lowest signed number
        else:
            sorted_times = []

        if x < 150:
            image =  pygame.image.load('images/move_right.jpg')
        elif x > 350:
            image =  pygame.image.load('images/move_left.jpg')
        elif y < 250:
            image =  pygame.image.load('images/move_back.jpg')
        elif y > 450:
            image = pygame.image.load('images/move_forward.jpg')
        else: #if centered
            image = pygame.image.load('images/nothing.png')
            self.screen.blit(image, (pygameWindowWidth / 2 , 0))
            if number == 0:
                image = pygame.image.load('images/Hand0.png')
            elif number == 1:
                image = pygame.image.load('images/Hand1.png')
            elif number == 2:
                image = pygame.image.load('images/Hand2.png')
            elif number == 3:
                image = pygame.image.load('images/Hand3.png')
            elif number == 4:
                image = pygame.image.load('images/Hand4.png')
            elif number == 5:
                image = pygame.image.load('images/Hand5.png')
            elif number == 6:
                image = pygame.image.load('images/Hand6.png')
            elif number == 7:
                image = pygame.image.load('images/Hand7.png')
            elif number == 8:
                image = pygame.image.load('images/Hand8.png')
            elif number == 9:
                image = pygame.image.load('images/Hand9.png')
            elif number == 10:
                image = pygame.image.load('images/nothing.png')
            if correctSigns > 1:
                image = FONT2.render(str(number), True, BLUE)



            if correctSigns >= 3:
                image = FONT2.render('X =  ' + str(basicNum1) + " " + type + " " + str(basicNum2), True, BLUE)
                self.screen.blit(image, (pygameWindowWidth / 2 + 150, pygameWindowDepth/2 + 100))
            else:
                self.screen.blit(image, (pygameWindowWidth / 2 + 150, pygameWindowDepth/2 + 150))


            # print(attempts)
            image = FONT2.render('Attempts: ' + str(int(attempts)), True, BLUE)
            self.screen.blit(image, (pygameWindowWidth / 2 , pygameWindowDepth / 2))

            if avgTime == 0:
                image = FONT3.render('Avg Time: ' + str("Not Set"), True, BLUE)
            else:
                image = FONT3.render('Avg Time: ' + str(int(math.floor(avgTime))), True, BLUE)

            self.screen.blit(image, (pygameWindowWidth/2 - 300, pygameWindowDepth / 2+ 200))

            image = FONT3.render('Ranks: ', True, BLUE)
            self.screen.blit(image, (pygameWindowWidth/2 - 300, pygameWindowDepth / 2 + 300))


            k = 360
            j = 1
            image = FONT3.render('Current Time: ' + str(int(math.floor(currentTime))), True, BLUE)
            self.screen.blit(image, (pygameWindowWidth / 2 - 300, pygameWindowDepth / 2 + 230))
            for i in sorted_times:
                image = FONT3.render(str(j) + ". " + str(i[0]) + ": " + str(i[1]), True, BLUE)
                self.screen.blit(image, (pygameWindowWidth / 2 - 300, pygameWindowDepth / 2 + k))
                k+=30
                j+=1


            return 1
        rfrsh = pygame.image.load('images/nothing.png')
        self.screen.blit(rfrsh, (pygameWindowWidth /2, pygameWindowDepth/2))
        self.screen.blit(image, (pygameWindowWidth / 2, 0))
        return 0

    def Put_Hand_Over(self):
        image = pygame.image.load('images/hand_over.png')
        self.screen.blit(image, (pygameWindowWidth / 2, 0))
