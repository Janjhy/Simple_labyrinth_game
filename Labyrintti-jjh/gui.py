
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *

class GUI(QtWidgets.QWidget):
    
    def __init__(self):
        super(GUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        
        #Buttons !WIP!
        moveDownBtn = QPushButton("Down")
        moveDownBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowDown)) 

        moveUpBtn = QPushButton("Up")
        moveUpBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowUp))
        
        moveLeftBtn = QPushButton("Left")
        moveLeftBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        
        moveRightBtn = QPushButton("Right")
        moveRightBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))   
         

        
        mainLayout = QVBoxLayout()
        mainLayout.addStretch(1)
        buttonLayout = QHBoxLayout()
        
        moveLayout = QVBoxLayout()
        
        moveUpLayout = QHBoxLayout()
        moveUpLayout.addSpacing(40)          
        moveUpLayout.addWidget(moveUpBtn)
        moveUpLayout.addStretch(1)
        moveLayout.addLayout(moveUpLayout)
        
        moveLRLayout = QHBoxLayout()
        moveLRLayout.addWidget(moveLeftBtn)
        moveLRLayout.addWidget(moveRightBtn)
        moveLRLayout.addStretch(1) 
               
        moveLayout.addLayout(moveLRLayout)
            
        moveDownLayout = QHBoxLayout() 
        moveDownLayout.addSpacing(40)        
        moveDownLayout.addWidget(moveDownBtn)
        moveDownLayout.addStretch(1)
        moveLayout.addLayout(moveDownLayout)  
        
        #horizontal.addWidget(view)
        buttonLayout.addLayout(moveLayout)    
            
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Game of Labyrinths')    
        self.show()
        