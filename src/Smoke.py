import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt
from .Settings import *

class Smoke(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
