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
		a_linedit = QLineEdit()
		b_linedit = QLineEdit()
		c_linedit = QLineEdit()

		#Add widget to group 
		grid_layout.addWidget(a_lbl,0,0)
		grid_layout.addWidget(b_lbl,0,1)
		grid_layout.addWidget(c_lbl,0,2)

		grid_layout.addWidget(a_linedit,1,0)
		grid_layout.addWidget(b_linedit,1,1)
		grid_layout.addWidget(c_linedit,1,2)

		#set Layout for Input group 
		input_grp.setLayout(grid_layout)

		#set solve button 
		solve_btn = QPushButton(" Solve ")
		solve_btn.clicked.connect(self.solve2dEquation)

		# Set layout for main window  
		glbl_box  = QVBoxLayout() 
		glbl_box.addWidget(title_lbl)
		glbl_box.addWidget(input_grp)
		glbl_box.addWidget(solve_btn)
		self.setLayout(glbl_box)
	
	def solve2dEquation(self) : 
		pass 


if __name__ == "__main__": 
	app = QApplication([])
	SQ  = SolveQuad() 
	app.exec() 
