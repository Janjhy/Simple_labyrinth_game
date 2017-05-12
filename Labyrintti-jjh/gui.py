
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore, QtGui
import PyQt5

from PyQt5.QtWidgets import QLabel
from PyQt5.Qt import *
from labyrinth import Labyrinth
from builtins import str
import pickle
from threading import Timer


class GUI(QtWidgets.QWidget):
    
    def __init__(self):
        super(GUI, self).__init__()
        
        
        self.mainLayout = QVBoxLayout()
        
        self.scene = QGraphicsScene()
        
        self.label = QLabel()
        self.label.setText("")
        
        self.level_label = QLabel()
        self.level_label.setText("")
        self.level = 0
        
        self.square_size = 16
        self.map_multiplier = 37
        
        
        self.map_size = self.map_multiplier * self.square_size
    
        self.scene.setSceneRect(0, 0, self.map_size, self.map_size)   

        
        self.view = QGraphicsView(self.scene)
        
        self.initUI()
        
        self.bgColor = QColor(229, 134, 12)
        self.bgBrush = QBrush(self.bgColor)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, self.bgBrush)
        self.setPalette(self.palette)

        self.setMinimumSize(self.size())
        self.move_up_hotkey = QShortcut(QKeySequence("Up"),self, self.move_player_up)
        self.move_down_hotkey = QShortcut(QKeySequence("Down"),self, self.move_player_down)
        self.move_right_hotkey = QShortcut(QKeySequence("Right"),self, self.move_player_right)
        self.move_left_hotkey = QShortcut(QKeySequence("Left"),self, self.move_player_left)
        
        
    def initUI(self):
        

        
 
        self.mainLayout.addWidget(self.view)
        self.view.adjustSize()
        self.view.show()

        self.initButtons() 
        self.setLayout(self.mainLayout)
        

        self.setWindowTitle('Game of Labyrinths')    

        self.show()
        

    def initButtons(self):
        
        self.moveDownBtn = QPushButton("Down")
        self.moveDownBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowDown)) 
        self.moveDownBtn.clicked.connect(self.move_player_down)

        self.moveUpBtn = QPushButton("Up")
        self.moveUpBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowUp))
        self.moveUpBtn.clicked.connect(self.move_player_up)

        
        self.moveLeftBtn = QPushButton("Left")
        self.moveLeftBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.moveLeftBtn.clicked.connect(self.move_player_left)
        
        self.moveRightBtn = QPushButton("Right")
        self.moveRightBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))   
        self.moveRightBtn.clicked.connect(self.move_player_right)
        
        self.changeLevelBtn = QPushButton("Change floor")
        self.changeLevelBtn.clicked.connect(self.change_level)
        
        self.useLadderBtn = QPushButton("Use ladder")
        self.useLadderBtn.clicked.connect(self.move_player_ladder)
        
        self.generateLabBtn = QPushButton("Generate new labyrinth")
        self.generateLabBtn.clicked.connect(self.generate_labyrinth)
        
        self.saveLabBtn = QPushButton("Save labyrinth")
        self.saveLabBtn.clicked.connect(self.save_labyrinth)
        
        self.loadLabBtn = QPushButton("Load labyrinth")
        self.loadLabBtn.clicked.connect(self.load_labyrinth)
        
        self.autoSolveBtn = QPushButton("Automatic solver")
        self.autoSolveBtn.clicked.connect(self.auto_solve)
        
        buttonLayout = QHBoxLayout()
        
        moveLayout = QVBoxLayout()
        
        moveUpLayout = QHBoxLayout()
        moveUpLayout.addSpacing(40)          
        moveUpLayout.addWidget(self.moveUpBtn)
        moveUpLayout.addStretch(1)
        moveLayout.addLayout(moveUpLayout)
        
        moveLRLayout = QHBoxLayout()
        moveLRLayout.addWidget(self.moveLeftBtn)
        moveLRLayout.addWidget(self.moveRightBtn)
        moveLRLayout.addStretch(1) 
               
        moveLayout.addLayout(moveLRLayout)
            
        moveDownLayout = QHBoxLayout() 
        moveDownLayout.addSpacing(40)        
        moveDownLayout.addWidget(self.moveDownBtn)
        moveDownLayout.addStretch(1)
        
        centerCtrlLayout = QVBoxLayout()
        centerCtrlLayout.addWidget(self.autoSolveBtn)
        centerCtrlLayout.addWidget(self.generateLabBtn)
        centerCtrlLayout.addWidget(self.saveLabBtn)
        centerCtrlLayout.addWidget(self.loadLabBtn)
        
        rightCtrlLayout = QVBoxLayout()
        rightCtrlLayout.addWidget(self.useLadderBtn)
        rightCtrlLayout.addWidget(self.changeLevelBtn)
        rightCtrlLayout.addWidget(self.label)
        rightCtrlLayout.addWidget(self.level_label)
        


        buttonLayout.addLayout(moveLayout) 
        buttonLayout.addStretch() 
        moveLayout.addLayout(moveDownLayout)  
        buttonLayout.addLayout(centerCtrlLayout)   
        buttonLayout.addStretch()   
        buttonLayout.addLayout(rightCtrlLayout)
          
                  
        self.mainLayout.addLayout(buttonLayout)
    
    
    def change_level(self):
        
        if(self.level == 0):
            self.level = 1
            self.level_label.setText("Floor 2")
        elif(self.level == 1):
            self.level = 0 
            self.level_label.setText("Floor 1")
                      
        
        self.update_labyrinth_gui()
      
    def update_labyrinth_gui(self):
        
        self.labyrinth.update_labyrinth(self.level)

    
    def move_player_up(self):
        
        self.labyrinth.move_player_up(self.label)
        self.update_labyrinth_gui()
 
    def move_player_down(self):
        
        self.labyrinth.move_player_down(self.label)
        self.update_labyrinth_gui()

    def move_player_right(self):
        
        self.labyrinth.move_player_right(self.label)
        self.update_labyrinth_gui()
        
    def move_player_left(self):
        
        self.labyrinth.move_player_left(self.label)   
        self.update_labyrinth_gui()              
        
    def move_player_ladder(self):    
        self.labyrinth.move_player_ladder(self.label)
        self.update_labyrinth_gui()    
     
    def generate_labyrinth(self):
        self.labyrinth = Labyrinth(self.map_multiplier, self.square_size, self.map_size, self.level_label, self.scene, self.style())   
        
 
            
        self.update_labyrinth_gui()
        
    def save_labyrinth(self):
        
        self.labyrinth.save_labyrinth()
        
    def load_labyrinth(self):
        
        self.labyrinth.load_labyrinth()
        self.update_labyrinth_gui()
        
    def auto_solve(self):
        self.labyrinth.automatic_solver()
         
          