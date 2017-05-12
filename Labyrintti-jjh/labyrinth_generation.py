'''
Created on 18 Mar 2017

@author: Jani
'''
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *
from labyrinth import *

class LabyrinthGenerator(object):
    
    def __init__(self, map_multiplier, square_size, level_label):
        
        self.map_multiplier = map_multiplier 
        self.square_size = square_size    
        self.level_label = level_label    
        self.wall_list = []
        
        self.squares = [None] * 2
        for x in range (len(self.squares)):     
            self.squares[x] = [None] * self.map_multiplier
            
            for y in range(self.map_multiplier): 
                self.squares[x][y] = [None] * self.map_multiplier
                
                for z in range (self.map_multiplier):
                    
                    self.squares[x][y][z] = Square(x, y, z)
                    self.squares[x][y][z].set_wall()
         

        self.squares[0][0][0].place_player()
        self.squares[0][0][0].set_visited()
        self.squares[0][0][0].remove_wall()
        self.squares[1][0][0].remove_wall()
        self.squares[1][0][0].set_visited()
        self.wall_list.append(self.squares[0][0][1])
        self.wall_list.append(self.squares[0][1][0])

        self.squares[1][self.map_multiplier - 1][self.map_multiplier - 1].remove_wall()
        self.squares[1][self.map_multiplier - 1][self.map_multiplier - 1].set_exit()
        
        self.squares[0][self.map_multiplier - 1][self.map_multiplier - 1].remove_wall()

                    
    def generate_level_one(self):
 
        
        checked = []         
        while(self.wall_list):
            
            
            

            check_wall = random.choice(self.wall_list)
            

            checked.append(check_wall)
            
            
            if(len(checked) > 500):
                break
            
                
            
            
   
            if((check_wall.get_y() + 1) < self.map_multiplier and (check_wall.get_y() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()].is_visited() == True)):
               
                self.calc_y_positive(check_wall)
                checked.remove(check_wall)

            elif((check_wall.get_y() + 1) < self.map_multiplier and (check_wall.get_y() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()].is_visited() == True)):
                
                self.calc_y_negative(check_wall)
                checked.remove(check_wall)       
 
            elif((check_wall.get_z() + 1) < self.map_multiplier and (check_wall.get_z() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1].is_visited() == True)):
                
                self.calc_z_positive(check_wall)
                checked.remove(check_wall)

                        
            elif((check_wall.get_z() + 1) < self.map_multiplier and (check_wall.get_z() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1].is_visited() == True)):
                
                self.calc_z_negative(check_wall)
                checked.remove(check_wall)
        
        if(len(checked) > 500):
            self.level_label.setText("Possible error in generation. Try again.")
            return self.squares
        else:
            self.level_label.setText("")    
        self.generate_level_two()
                             
        self.add_ladders()   
        return self.squares 
    
    def generate_level_two(self):
        self.wall_list.append(self.squares[1][1][0])
        self.wall_list.append(self.squares[1][0][1])        
        
        checked = []
        while(self.wall_list):
            

            
            check_wall = random.choice(self.wall_list)
            

            checked.append(check_wall)
            
            if(len(checked) > 500):
                
                break
   
            if((check_wall.get_y() + 1) < self.map_multiplier and (check_wall.get_y() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()].is_visited() == True)):
                self.calc_y_positive(check_wall)
                checked.remove(check_wall)

            elif((check_wall.get_y() + 1) < self.map_multiplier and (check_wall.get_y() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()].is_visited() == True)):
                self.calc_y_negative(check_wall)
                checked.remove(check_wall)        
 
            elif((check_wall.get_z() + 1) < self.map_multiplier and (check_wall.get_z() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1].is_visited() == True)):
                self.calc_z_positive(check_wall)
                checked.remove(check_wall)
                                        
            elif((check_wall.get_z() + 1) < self.map_multiplier and (check_wall.get_z() - 1 > (-1)) and (self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1].is_visited() == True)):
                self.calc_z_negative(check_wall)
                checked.remove(check_wall)
                
        if(len(checked) > 500):
            self.level_label.setText("Possible error in generation. Try again.")
        else:
            self.level_label.setText("")     
        return self.squares                
    
    def calc_y_positive(self, check_wall):
        if(check_wall.get_y() + 1 < self.map_multiplier and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()].is_visited() == True):
            
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()].set_visited()
            self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()])
            return
        else:
            
            self.wall_list.remove(check_wall)
            check_wall.remove_wall()
  
            if(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()] in self.wall_list):
                
                self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()])
            self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()].set_visited()
            self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z()].remove_wall()
                    

                    
            if((check_wall.get_y() + 2 < self.map_multiplier) and self.squares[check_wall.get_x()][check_wall.get_y() + 2][check_wall.get_z()].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() + 2][check_wall.get_z()].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() + 2][check_wall.get_z()])
                        
            if(check_wall.get_z() + 1 < self.map_multiplier and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() + 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() + 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() + 1])                    
                     
            if(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1])


                        
    def calc_y_negative(self, check_wall):
        if(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()].is_visited() == True):
            
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()].set_visited()
            self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()])                    
            return
        else:
            
            self.wall_list.remove(check_wall)
            check_wall.remove_wall()
            self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()].set_visited()
            self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()].remove_wall()
                    
            if(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()] in self.wall_list):
                self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z()])
                                  

                    
            if(self.squares[check_wall.get_x()][check_wall.get_y() - 2][check_wall.get_z()].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() - 2][check_wall.get_z()].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() - 2][check_wall.get_z()])
                        
            if(check_wall.get_z() + 1 < self.map_multiplier and self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() + 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() + 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() + 1])                    
                     
            if(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1])
                
    def calc_z_negative(self, check_wall):
                        
        if(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1].is_visited() == True):
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()].set_visited()
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()].set_visited()
            self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()])                    
                    
            
            return
        else:
            
            self.wall_list.remove(check_wall)
            check_wall.remove_wall()
                    
            if(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1] in self.wall_list):
                self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1])
                                   
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1].set_visited()
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 1].remove_wall()
                    
            if(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 2].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 2].is_visited() == False):
                        self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() - 2])
                        
            if(check_wall.get_y() + 1 < self.map_multiplier and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() - 1])                    
                     
            if(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() - 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() - 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() - 1])   
                
    def calc_z_positive(self, check_wall):    
         
        if(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1].is_visited() == True):
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()].set_visited()
            self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z()])                    
            
            return
        else:
            
            self.wall_list.remove(check_wall)
            check_wall.remove_wall()
                    
            if(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1] in self.wall_list):
                self.wall_list.remove(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1])
                
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1].set_visited()
            self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 1].remove_wall()
                    
            if((check_wall.get_z() + 2) < self.map_multiplier and self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 2].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 2].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y()][check_wall.get_z() + 2])
                        
            if((check_wall.get_y() + 1) < self.map_multiplier and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() + 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() + 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() + 1][check_wall.get_z() + 1])                    
                     
            if(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() + 1].is_wall() == True and self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() + 1].is_visited() == False):
                self.wall_list.append(self.squares[check_wall.get_x()][check_wall.get_y() - 1][check_wall.get_z() + 1])

    def add_ladders(self):
        
        for y in range (self.map_multiplier):
            for z in range (self.map_multiplier):
                
                if(self.squares[0][y][z].is_wall() == False and self.squares[1][y][z].is_wall() == False):
                    rand = randrange(0, 20, 1)
                    if(rand < 1):
                        self.squares[0][y][z].set_ladder()
                        self.squares[1][y][z].set_ladder()              