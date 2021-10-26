import sys 
from PyQt5.QtWidgets import (QApplication,
	QWidget, 
	QLabel, 
	QPushButton, 
	QLineEdit, 
	QVBoxLayout, 
	QGridLayout,
	QGroupBox)
from PyQt5.QtGui import QFont

class SolveQuad(QWidget):
	""" doc string to do later """ 

	def __init__(self): 
		super().__init__()
		self.initializeUI()

	def initializeUI(self): 
		self.setGeometry(100,100,400,300)
		self.setWindowTitle(" Quadratique Equation Solver 1.0 ")
		self.setUI()

		self.show()

	def setUI(self): 
		
		# Set title 
		title_lbl = QLabel("2D Equation Solver",self)
		title_lbl.setFont(QFont("arial",20))

		# set Input group to get coefficient values from user 
		input_grp   = QGroupBox()
		grid_layout = QGridLayout()
		
		# Coefficent label
		a_lbl  = QLabel("a")
		b_lbl  = QLabel("b")
		c_lbl  = QLabel("c")

		# To get coefficient from the user 
		self.a_linedit = QLineEdit()
		self.b_linedit = QLineEdit()
		self.c_linedit = QLineEdit()

		#Add widget to group 
		grid_layout.addWidget(a_lbl,0,0)
		grid_layout.addWidget(b_lbl,0,1)
		grid_layout.addWidget(c_lbl,0,2)

		grid_layout.addWidget(self.a_linedit,1,0)
		grid_layout.addWidget(self.b_linedit,1,1)
		grid_layout.addWidget(self.c_linedit,1,2)

		#set Layout for Input group 
		input_grp.setLayout(grid_layout)

		#set solve button 
		solve_btn = QPushButton(" Solve ")
		solve_btn.clicked.connect(self.solve2dEquation)

		#set solution 

		self.solution = QLabel("")

		# Set layout for main window  
		glbl_box  = QVBoxLayout() 
		glbl_box.addWidget(title_lbl)
		glbl_box.addWidget(input_grp)
		glbl_box.addWidget(solve_btn)
		glbl_box.addWidget(self.solution)
		self.setLayout(glbl_box)
	
	def solve2dEquation(self) :  
		import math 

		try : 
			a = float(self.a_linedit.text())
			b = float(self.b_linedit.text())
			c = float(self.c_linedit.text())
		except ValueError : 
			self.solution.setText("You must give a numerical value !!")
			return "" 

		try : 
			delta = b**2 - 4*a*c

			if delta < 0 : 
				self.solution.setText(" Pas de solutions reelles ")
			elif delta == 0:
				x = -b/(2*a)
				x = str(x)
				self.solution.setText("solution unique : " +  x ) 
			else : 
				x1 = (-b - math.sqrt(delta))/(2*a)
				x1 = str(x1)
				x2 = str((-b + math.sqrt(delta))/(2*a))
				x2 = str(x2)
				self.solution.setText(f'x1 =  {x1}  ;   x2 = {x2}' )
		except ZeroDivisionError:
			self.solution.setText(" a must be different from 0!!")
			return "" 



if __name__ == "__main__": 
	app = QApplication([])
	SQ  = SolveQuad() 
	app.exec() 
