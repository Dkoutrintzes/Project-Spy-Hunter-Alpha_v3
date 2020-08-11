import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt
from .Settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, name, x, y, id, speed):
        super().__init__()
        self.image = pygame.image.load(name)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed
        self.speed_y = speed
        self.id = id

    def update(self):
        if self.id == 0:
            self.rect.y += self.speed_y
        elif self.id == 1:
            self.rect.x += self.speed_x

    def get_y(self):
        return self.rect.y