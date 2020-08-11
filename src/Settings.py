import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt

WIDTH = 1200
HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (117, 70, 0)

SCORE = 0

Level1 = [['src/Part_0.png', 'straight_road',0,0,1],
          ['src/Part_1.png', 'turn_left_road',0,0,2],
          ['src/Part_2.png', 'turn_right_road',0,0,3],
          ['src/Part_3.png', 'cross_road',0,0,4],
          ['src/Part_4.png', 'cross_road_to_right_road',0,0,5],
          ['src/Part_5.png', 'right_to_middle_road',0,0,0]]

Enemy_spawn = [[1,'top',55],
               [4,'bottom',85],
               [0,'top',20]]


# Σε αυτο το σημειο απλα κανω την ζωη μου δυσκολη
# Creating polygons for the hit box of every type of road

def create_polygon(rect):
    new_polygon = [[rect[0], rect[1]],
                   [rect[0] + rect[2], rect[1]],
                   [rect[0], rect[1] + rect[3]],
                   [rect[0] + rect[2], rect[1] + rect[3]]]

    return new_polygon


def straight_road(y_start):
    rect_list = []
    for y in range(-400, 400):
        x = 300
        rect = [x, y + 400 + y_start , 600, 1]
        rect_list.append([rect])
    #print(rect_list)
    return rect_list


def turn_left_road(y_start):
    rect_list = []
    for y in range(-400, 400):
        x = (y + 110 - 0.0000005 * y ** 3 - 0.66 * y)
        rect = [x + 100, y + 400+ y_start, 600, 1]
        rect_list.append([rect])
    #print(rect_list)
    return rect_list


def turn_right_road(y_start):
    rect_list = []
    for y in range(-400, 400):
        x = -(y - 190 - 0.0000005 * y ** 3 - 0.4 * y)
        rect = [x + 100, y + 400+ y_start, 600, 1]
        rect_list.append([rect])
    #print(rect_list)
    return rect_list


def cross_road(y_start):
    rect_list = []
    dead_list = []
    for y in range(-400, 400):
        x = (y + 150 - 0.0000015 * y ** 3 - 0.13 * y)
        rect = [x + 100, y + 400+ y_start, 420, 1]
        rect_list.append([rect])
    for y in range(-400, 400):
        x = -(y-670-0.0000002*y**3-0.85*y)
        rect = [x+100,y+400 + y_start,400,1]
        dead_list.append([rect])
    return rect_list,dead_list


def cross_road_to_right_road(y_start):
    rect_list = []
    for y in range(-400, 400):
        x = -(y + 0.0000005 * y ** 3 - 0.8 * y)
        rect = [x + 100, y + 400+ y_start, 420 + (150 - (y + 400) * 0.18), 1]
        rect_list.append([rect])

    return rect_list


def right_to_middle_road(y_start):
    rect_list = []
    for y in range(-400, 400):
        x = -((0.13 * y - 170) + abs(0.0000002 * y ** 3))
        rect = [x + 100, y + 400+ y_start, 590, 1]
        rect_list.append([rect])

    return rect_list
