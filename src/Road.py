import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt
from .Settings import *

class Road():
    def __init__(self,image,type_road,x,y,next):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.hit_list = []
        self.dead_road = []
        self.hit_boxes = pygame.sprite.Group()
        self.dead_hit_boxes = pygame.sprite.Group()
        self.type_road = type_road
        self.y = y - HEIGHT
        self.next = next
        self.rect.y = self.y
        if self.type_road == 'straight_road':
            self.hit_list = straight_road(self.y)
            self.create_hit_boxes()
        elif self.type_road == 'turn_left_road':
            self.hit_list = turn_left_road(self.y)
            self.create_hit_boxes()
        elif self.type_road == 'turn_right_road':
            self.hit_list = turn_right_road(self.y)
            self.create_hit_boxes()
        elif self.type_road == 'cross_road':
            self.hit_list,self.dead_road = cross_road(self.y)
            self.create_hit_boxes()
        elif self.type_road == 'cross_road_to_right_road':
            self.hit_list = cross_road_to_right_road(self.y)
            self.create_hit_boxes()
        elif self.type_road == 'right_to_middle_road':
            self.hit_list = right_to_middle_road(self.y)
            self.create_hit_boxes()
        self.x = x


    def create_hit_boxes(self):
        for rect in self.hit_list:
            #print(rect)
            new_rect = Rect(rect[0][0],rect[0][1],rect[0][2],rect[0][3])
            self.hit_boxes.add(new_rect)
        if self.next == 4:
            for rect in self.dead_road:
                #print(rect)
                new_rect = Rect(rect[0][0], rect[0][1], rect[0][2], rect[0][3])
                self.dead_hit_boxes.add(new_rect)
            #print(self.dead_hit_boxes,self.hit_boxes)
        #print(self.hit_boxes)

    def get_y_line(self,y):
        '''if self.next == 4:
            rect = []
            for rect in self.hit_list:
                if rect[0][1] == y:
                    rect.append(rect)
                for i in range(len(rect)):
                    print('hello',rect[i],i)
            return rect[0]
        else:'''
        for rect in self.hit_list:
            if rect[0][1] == y:
                return rect[0]

    def get_x_line(self,x):
        for rect in self.hit_list:
            if rect[0][0] == x:
                return rect[0]
    def get_y(self):
        return self.rect.y


    def draw(self,screen):
        screen.blit(self.image,[self.x,self.y])

    def update(self):
        self.y += 5
        self.rect.y += 5
        self.hit_boxes.update()
        self.dead_hit_boxes.update()
        for rect in self.hit_list:
            rect[0][1] += 5

    def get_y(self):
        return self.y

    def get_next(self):
        return self.next
    def check_collide(self,item_list,check_dead_zone):
        #print(check_dead_zone)
        hit_list = pygame.sprite.Group()
        for item in item_list:
            if pygame.sprite.spritecollide(item,self.hit_boxes,False):
                hit_list.add(item)
        if check_dead_zone:
            #print('hello',item_list)
            for item in item_list:
                #print('here',pygame.sprite.spritecollide(item,self.dead_hit_boxes,False) ,item)
                if  pygame.sprite.spritecollide(item,self.dead_hit_boxes,False) :
                    #print('hello')
                    hit_list.add(item)
        return hit_list


    '''def draw(self,screen):
        print(self.rect.x,self.rect.y)
        counter = 0
        screen.blit(self.image, [self.rect.x, self.rect.y])
        for i in self.hit_boxes:
            i.draw(screen)
            counter += 1
        #print(counter)'''


class Rect(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y = y
        #self.r =[x,y,width,800]
        self.rect =  pygame.Rect(x,y,width,2)
    def update(self):
        self.rect.y += 5
        #self.r[1] += 5


    '''def draw(self,screen):
        #print(self.r)
        pygame.draw.rect(screen,GREEN,self.r)'''
