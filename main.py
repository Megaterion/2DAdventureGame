import pygame
import sys
from settings import *

class Game:
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WITH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('red')
            pygame.display.update()
            self.clock.tick(FPS)

