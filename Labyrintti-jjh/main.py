'''
Created on 18 Mar 2017

@author: Jani
'''
import sys
from gui import GUI
from PyQt5.QtWidgets import QApplication

def main():
    
        global app
        app = QApplication(sys.argv)
        
        gui = GUI()
        gui.show()
        sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()