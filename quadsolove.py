import sys 
from PyQt5.QtWidgets import (QApplication,
	QWidget, 
	QLabel, 
	QPushButton, 
	QTextEdit, 
	QVBoxLayout, 
	QGridLayout)
from PyQt5.QtGui import QFont

print("tout va bien ")

class SolveQuad(QWidget):
	""" doc string to do later """ 

	def __init__(self): 
		super().__init__()
		self.initializeUI()

	def initializeUI(self): 
		self.setGeometry(100,100,400,400)
		self.setWindowTitle(" Quadratique Equation Solver 1.0 ")

		self.show()



if __name__ == "__main__": 
	app = QApplication([])
	SQ  = SolveQuad() 
	app.exec() 
