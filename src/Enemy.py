import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt
from .Settings import *
from .Bullet import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, road_ract_pos, road_side, road_pos):
        super().__init__()
        self.road_side = road_side
        self.image = pygame.image.load(name)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.id = random.randrange(10000000000000, 20000000000000)
        self.rect.x = road_ract_pos[0] + road_pos
        #print(self.road_side)
        if self.road_side == 'top':
            self.rect.y = road_ract_pos[1] - 100
        elif self.road_side == 'bottom':
            #print('im here')
            self.rect.y = 799

        self.speed_x = 2
        self.speed_y = 2.5
        self.road_pos = road_pos
        self.is_hunting = False

    def get_id(self):
        return self.id

    def res_pos(self):

        self.rect.x = 0
        self.rect.y = 0

    def update(self, road):
        temp_list = pygame.sprite.Group()
        temp_list.add(self)
        i = 0

        rect = road.get_y_line(self.rect.y - i)
        '''while not rect:
            i += 1
            print(i)
            print(road,road.get_next())
            rect = road.get_y_line(self.rect.y+i)'''
        if not self.is_hunting:
            if self.rect.y > 600:
                self.speed_y = -2.5
            elif self.rect.y < 200:
                self.speed_y = 2.5

            # print(road.get_y_line(self.rect.y),self.rect.y,road.get_next())

            if self.rect.y < 100 and self.road_side == 'top':
                self.rect.y += 2.5
                self.rect.x = rect[0] + (rect[2] * self.road_pos / 100)
            elif self.rect.y > 600 and self.road_side == 'bottom':
                self.rect.y -= 2.5
                self.rect.x = rect[0] + (rect[2] * self.road_pos / 100)
            elif 100 <= self.rect.y <= 600:
                self.rect.y += self.speed_y
                # print('this is',rect[0] + rect[2] - self.road_pos)
                if rect:
                    self.rect.x = rect[0] + (rect[2] * self.road_pos / 100)

        elif self.is_hunting:
            if rect:
                self.rect.x = rect[0] + (rect[2] * self.road_pos / 100)
            if self.rect.y > self.pleyer_is:
                self.rect.y -= 1
            elif self.rect.y < self.pleyer_is:
                self.rect.y += 1
            else:
                self.rect.y += 0

    def hunt_player(self, is_hunting, player_y, ):
        self.pleyer_is = player_y
        self.is_hunting = is_hunting

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_speed_x(self, new_speed):
        self.speed_x = new_speed

    def revers_speed_x(self):
        self.speed_x = - self.speed_x

    def revers_speed_y(self):
        self.speed_y = - self.speed_y

    def enemy_fire(self, x_player):
        if self.rect.x <= x_player:
            bullet = Bullet('src/bullet_right.png', self.rect.x + 35, self.rect.y + 50, 1, +10)
        elif self.rect.x > x_player:
            bullet = Bullet('src/bullet_left.png', self.rect.x - 35, self.rect.y + 50, 1, -10)
        return bullet

    def get_hunt(self):
        return self.is_hunting
