# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:40:23 2020

@author: matzo
"""
class Obstacle:
    def __init__(self, obstacle_string):
        x1, y1, x2, y2, x3, y3 = obstacle_string.split(' ')
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)