'''
Created on 27 Apr 2017

@author: Jani
'''

import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *



class Square(object):
    
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        self.player = False
        self.wall = False
        self.ladder = False 
        self.exit = False
        self.visited = False
        
    
    def set_visited(self):
        
        self.visited = True
     
    def is_visited(self):
        
        return self.visited
     
    def set_exit(self):
        self.exit = True
        
    def is_exit(self):
        
        
        return self.exit
             
    def set_wall(self):
        
        self.wall = True
        
    def remove_wall(self):
        
        self.wall = False    
        
    def get_x(self):
        
        return self.x   
    
    def get_y(self):
        
        return self.y 
    
    def get_z(self):
        
        return self.z
    
    def set_ladder(self):
        
        self.ladder = True  
    
    def is_ladder(self):
        
        return self.ladder
    
    def remove_ladder(self):
        
        self.ladder = False
    
    def is_wall(self):
        
        return self.wall
        
    def place_player(self):
        
        self.player = True
        
    def is_player(self):
        
        return self.player
    
    def remove_player(self):
        self.player = False