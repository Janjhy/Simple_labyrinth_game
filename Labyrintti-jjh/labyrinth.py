'''
Created on 27 Apr 2017

@author: Jani
'''
from squares import Square
import random
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *
from random import randrange
import gui
from labyrinth_generation import LabyrinthGeneration
import pickle
import time




class Labyrinth(object):

    def __init__ (self, map_multiplier, square_size, map_size, level_label, scene, style):
        
        self.level_label = level_label
        self.map_size = map_size
        self.map_multiplier = map_multiplier 
        self.square_size = square_size
        self.scene = scene
        self.style = style

        

        self.generated_labyrinth =  LabyrinthGeneration(self.map_multiplier, self.square_size, self.level_label)
        
            
        self.squares = self.generated_labyrinth.generate_level_one()
          
              
        self.player_square = self.squares[0][0][0]
        


    
    def get_square(self, x, y, z):
        
        return self.squares[x][y][z]
    
    def move_player_down(self, label):
        
        current_square = self.player_square
        
        
        if((self.player_square.get_z() + 1) > (self.map_multiplier - 1)):
            
            label.setText("Out of bounds") 
            
        elif(self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].is_wall() == True):
            label.setText("Can't go down")
            
                
        else:
            self.player_square = self.squares[current_square.get_x()][current_square.get_y()][current_square.get_z() + 1]
            current_square.remove_player()
            self.player_square.place_player()     
            label.setText("Moved down")
            
            if(self.player_square.is_exit() == True):
                label.setText("You got to the exit!")            
        
        
    def move_player_up(self, label):
        current_square = self.player_square
        
        if((self.player_square.get_z() - 1) < 0):
            label.setText("Out of bounds")
            
        elif(self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].is_wall() == True):
            label.setText("Can't go up")
                
        else:
            self.player_square = self.squares[current_square.get_x()][current_square.get_y()][current_square.get_z() - 1]
            current_square.remove_player()
            self.player_square.place_player()
            label.setText("Moved up")
            
            if(self.player_square.is_exit() == True):
                label.setText("You got to the exit!")            
        
    def move_player_right(self, label):
        
        current_square = self.player_square
                 
        
        
            
        if((self.player_square.get_y() + 1) > (self.map_multiplier - 1)):
            label.setText("Out of bounds")
            
        elif(self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].is_wall() == True):
            label.setText("Can't go right")
                
        else:
            self.player_square = self.squares[current_square.get_x()][current_square.get_y() + 1][current_square.get_z()]
            current_square.remove_player()
            self.player_square.place_player()        
            label.setText("Moved right")
            
            if(self.player_square.is_exit() == True):
                label.setText("You got to the exit!")            
        
    def move_player_left(self, label):    
        
        current_square = self.player_square    
            
        if((self.player_square.get_y() - 1) < 0):
            label.setText("Out of bounds")
            
        elif(self.squares[self.player_square.get_x()][(self.player_square.get_y()) - 1][self.player_square.get_z()].is_wall() == True):
            label.setText("Can't go left")
                
        else:
            self.player_square = self.squares[current_square.get_x()][current_square.get_y() - 1][current_square.get_z()]
            current_square.remove_player()
            self.player_square.place_player()    
            label.setText("Moved left")
            
            if(self.player_square.is_exit() == True):
                label.setText("You got to the exit!")
            
    def move_player_ladder(self, label):
        
        current_square = self.player_square    
            
        if(self.player_square.is_ladder() == False):
            label.setText("No ladder")
                
        elif(self.player_square.get_x() == 0):
            self.player_square = self.squares[current_square.get_x() + 1][current_square.get_y()][current_square.get_z()]
            current_square.remove_player()
            self.player_square.place_player()    
            label.setText("Used ladder")    
                
        elif(self.player_square.get_x() == 1):
            self.player_square = self.squares[current_square.get_x() - 1][current_square.get_y()][current_square.get_z()]
            current_square.remove_player()
            self.player_square.place_player()    
            label.setText("Used ladder")             
    
    def update_labyrinth(self, level):


        lgreen = QBrush(QColor(126,216,114)) 
        dgrey = QBrush(QColor(20,20,20)) 
         
        player_colour = QBrush(QColor(27, 114, 214))       
        exit_colour = QBrush(QColor(160,8,102))

        for y in range (self.map_multiplier):
            for z in range (self.map_multiplier):
              


                gsquare = QGraphicsRectItem((self.squares[level][y][z].get_y() * self.square_size), (self.squares[level][y][z].get_z() * self.square_size), self.square_size, self.square_size)

                

   
                if(self.get_square((self.player_square.get_x()), y, z).is_ladder() == True):
                    
                    p_icon = QPixmap
                    
                    s_icon = self.style.standardIcon(QStyle.SP_FileDialogDetailedView)
                    p_icon = s_icon.pixmap(s_icon.actualSize(QSize(self.square_size, self.square_size)))
                    l_icon = QGraphicsPixmapItem(p_icon)
                    
                    
                    self.scene.addItem(l_icon)
                    l_icon.setPos(y * self.square_size , z * self.square_size)   
                elif(self.get_square(level, y, z).is_exit() == True):  
                    gsquare.setBrush(exit_colour)
                                          
                elif(self.get_square((level), y, z).is_player() == True):
                    gsquare.setBrush(player_colour)  
                    player_colour = QBrush(QColor(27, 114, 214))                   
                elif(self.get_square(level, y, z).is_wall() == True):
                    gsquare.setBrush(dgrey)                  
                

                else:
                    gsquare.setBrush(lgreen) 
                
 
                
                   

                self.scene.addItem(gsquare)
                            
    def get_player(self):
        
        return self.player_square
    
    def get_squares(self):
        
        return self.squares

                    
    def save_labyrinth(self):
        
        open('save_file.pickle', 'w').close()
        to_be_saved = self.squares

        with open('save_file.pickle', 'wb') as handle:
            
                pickle.dump(to_be_saved, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    def load_labyrinth(self):
        
        with open('save_file.pickle', 'rb') as handle:
            to_be_used = pickle.load(handle)
        self.squares = to_be_used
                   
    def automatic_solver(self):
        

           
        
        facing = "Down"
        while(self.player_square.is_exit() == False):

            
            
            if(self.player_square.get_x() == 0 and self.player_square.is_ladder() == True):

                self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z()].remove_player()
                self.squares[self.player_square.get_x() + 1][self.player_square.get_y()][self.player_square.get_z()].place_player()
                self.player_square = self.squares[self.player_square.get_x() + 1][self.player_square.get_y()][self.player_square.get_z()]
                
                
                
            elif(facing == "Down"):

                if(self.player_square.get_y() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].is_wall() == False):   


                    self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()]
                    facing = "Right"
                    
                elif(self.player_square.get_z() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].is_wall() == False): 
 
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1]
                    facing = "Down" 
                                                            
                elif(self.player_square.get_y() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].is_wall() == False):  

                    self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()]
                    facing = "Left"  
                                                                               
                    
                elif(self.player_square.get_z() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].is_wall() == False): 
 
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1]
                    facing = "Up"
                   
 
                    
                    
            elif(facing == "Right"):
                
                if(self.player_square.get_z() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1]
                    facing = "Up"

                elif(self.player_square.get_y() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].place_player() 
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()]
                    facing = "Right" 
                                        
                elif(self.player_square.get_z() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1]
                    facing = "Down"
                    

                                       
                elif(self.player_square.get_y() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].place_player() 
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()]
                    facing = "Left"                                                              
                    
            elif(facing == "Up"):
                
                if(self.player_square.get_y() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()]
                    facing = "Left"     
                    
                elif(self.player_square.get_z() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].place_player() 
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1]
                    facing = "Up"                
                    
                elif(self.player_square.get_y() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()]
                    facing = "Right" 
                    

                    
                elif(self.player_square.get_z() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1]
                    facing = "Down"  
                                      
            elif(facing == "Left"):
                
                if(self.player_square.get_z() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1].place_player() 
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() + 1]
                    facing = "Down"
                    
                elif(self.player_square.get_y() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].is_wall() == False):                       
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() - 1][self.player_square.get_z()]
                    facing = "Left"                                         
                elif(self.player_square.get_z() - 1 > (-1) and self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1].place_player()
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y()][self.player_square.get_z() - 1]
                    facing = "Up"
                    


                    
                elif(self.player_square.get_y() + 1 < self.map_multiplier and self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].is_wall() == False):   
                    
                    self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()].place_player() 
                    self.player_square = self.squares[self.player_square.get_x()][self.player_square.get_y() + 1][self.player_square.get_z()]
                    facing = "Right"                                                                                                                              
 
        self.update_labyrinth(self.player_square.get_x())
                                                       