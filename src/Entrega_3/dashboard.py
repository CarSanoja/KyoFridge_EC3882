import sys
from PyQt5 import QtCore, QtWidgets, uic
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget
import numpy as np

qtCreatorFile = "dash.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.electret_plot.setXRange(0,10)
		self.electret_plot.setYRange(0,10)
		graf = self.electret_plot.getPlotItem()
		self.electret_plot.plot(np.random.normal(size=100), clear=True )


#	def imprimir(self):
#		self.salida.setText("total_price_string")

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
sys.exit(app.exec_())