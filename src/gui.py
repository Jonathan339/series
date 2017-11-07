import sys
from PyQt5.QtWidgets import QAapplication, QMainWindow, QAction, QMessageBox, QApplication
from PyQt5 import uic 
from PyQt5.QtGui import QIcon

class Ventana(QMainWindow):
	def __ini__(self):
		super().__init__()

	def initUI(self):
		self.resize(600, 500)





if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())