import pygame
import Game

WIDTH = 20
HEIGHT = 50

class Attack(object):
    
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
    
    def update(self):
        #move according to dir
        pass
    
    def render(self, screen):
        rect = pygame.rect.Rect(self.pos, (WIDTH, HEIGHT))
        pygame.draw.rect(screen, Game.CYAN, rect)