import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt
from .Settings import *
from .Bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.image = pygame.image.load(name)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.alive = True

    def player_movement(self,x,y):

        self.speed_x += x
        self.speed_y += y

    def update(self):
        if self.alive is True:
            if self.speed_x < 0:
                # Turns Left
                self.rect.x += self.speed_x
                self.turn_car('Left')
            elif self.speed_x > 0:
                # Turns Right
                self.rect.x += self.speed_x
                self.turn_car('Right')
            else:
                # Car is going Straight
                self.turn_car("Straight")
        else:
            self.speed_x = -10.5
        self.rect.y += self.speed_y

    def turn_car(self,side):
        if side == 'Right':
            self.image = pygame.image.load('src/player_right.png')
        elif side == 'Left':
            self.image = pygame.image.load('src/player_left.png')
        elif side == 'Straight':
            self.image = pygame.image.load('src/player.png')

    def fire_lasers(self):
        if self.alive:
            bullets = pygame.sprite.Group()
            for i in [15,40]:
                bullet  = Bullet('src/Bullet.png',self.rect.x+i,self.rect.y,0,-10)
                bullets.add(bullet)
            return bullets

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def check_isalive(self):
        return self.alive

    def lost(self):
        self.alive = False