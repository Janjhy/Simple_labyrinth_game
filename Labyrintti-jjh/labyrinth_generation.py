'''
Created on 18 Mar 2017

@author: Jani
'''
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import *


class GUI(QtWidgets.QMainWindow):
    
    
    def __init__(self):
        
        super().__init__()
        
        self.initUI()



    def initUI(self):
        
        #QMainwindow needs a central widget
        self.setCentralWidget(QtWidgets.QWidget())
        
        #Add a horizontal box layout
        self.horizontal = QtWidgets.QHBoxLayout()
        
        #Set window title
        self.setWindowTitle("Game of Labyrinths")
        
        #Sets the initial size of the main window
        self.setMinimumSize(300, 300)
        
        #self.scene = QtWidgets.QGraphicsScene()
        #self.scene.setSceneRect(0, 0, 200, 200)
        
        #self.view = QtWidgets.QGraphicsView(self.scene, self)
        
        
        #Sets the general background colour for the window
        self.bgColor = QColor(229, 134, 12)
        self.bgBrush = QBrush(self.bgColor)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, self.bgBrush)
        self.setPalette(self.palette)
        
        
        #Buttons !WIP!
        self.moveDownBtn = QPushButton("Down", self)
        self.moveDownBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowDown))

        self.moveUpBtn = QPushButton("Up", self)
        self.moveUpBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowUp))
        
        self.moveLeftBtn = QPushButton("Left", self)
        self.moveLeftBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        
        self.moveRightBtn = QPushButton("Right", self)
        self.moveRightBtn.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))    
        
        #Movement button layout
        
        self.moveLayout = QtWidgets.QVBoxLayout()
        self.moveLayout.addStretch(1)
        self.moveLayout.addWidget(self.moveUpBtn)
        
        self.moveLRLayout = QtWidgets.QHBoxLayout()
        self.moveLRLayout.addStretch(1)
        self.moveLRLayout.addWidget(self.moveLeftBtn)
        #self.moveLRLayout.addWidget(self.moveRightBtn)
                
        self.moveLayout.addLayout(self.moveLRLayout)
             
        self.moveLayout.addWidget(self.moveDownBtn)
               



        
        #self.view.adjustSize()
        
        #self.view.show()
        
        #self.horizontal.addWidget(self.view)
        self.horizontal.addLayout(self.moveLayout)        
        #self.setLayout(self.horizontal)
        self.show()