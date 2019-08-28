import pygame

class PYGAME_WINDOW:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300,100))

    def Prepare(self):
        pygame.event.get()
        self.bg_color = 255, 255, 0
        self.screen.fill(self.bg_color)

    def Reveal(self):
        pygame.display.update()