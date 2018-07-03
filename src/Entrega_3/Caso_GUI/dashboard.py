import sys
from PyQt5 import QtCore, QtWidgets, uic
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget
import numpy as np
import matplotlib.pyplot as plt
import json

qtCreatorFile = "dash.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.electret_plot.setXRange(0,4)
		self.electret_plot.setYRange(0,5)
		self.graf = self.electret_plot.getPlotItem()
		self.on.clicked.connect(self.plot_electret)
		self.puerta.clicked.connect(self.data_door)
		self.Temp_bot.clicked.connect(self.data_image)

	def data_image(self):
		image_path = 'c:/home/carlos/Imágenes/img.jpeg' #path to your image file
		self.imagen.plot(image_path)


	def data_temp(self):
		with open('data.txt') as json_file:  
			signal = json.load(json_file)
		self.temp_grados.setText(str(str(signal["analogico_2"][0])+"°"))
		if signal["analogico_2"][0] > 35:
			self.temp_bar.setValue(66)
			self.temp_suggestion.setText("Take care, it's hot")

	def data_door(self):
		with open('data.txt') as json_file:  
			signal = json.load(json_file)
		if signal["digital_1"][0] == 1:
			print("puerta abierta")
			self.door_status.setText(str("Puerta Abierta"))	
		else:
			print("puerta cerrada")
			self.door_status.setText(str("Puerta Cerrada"))

	def plot_electret(self):
		file2 = open("time_base_data.txt","r")
		t2_read = float(file2.read())
		with open('data.txt') as json_file:  
			signal = json.load(json_file)
		self.electret_plot.setXRange(0,t2_read)
		self.electret_plot.setYRange(0,3)
		self.electret_plot.plot([t*0.0005 for t in range(0,400, 1)]
							,signal["analogico_1"][len(signal["analogico_1"])-400:]
							, 'r-', label='Electret', clear=True )
		if signal["digital_2"][0] == 1:
			data_image = 1
			with open('data_im.txt', 'w') as outfile:  
				json.dump(data_image, outfile)
			self.electret_enable.setText(str("Esperando comando de voz"))
		else:
			self.electret_enable.setText(str(" No Escuchando "))
			data_image = 0
			with open('data_im.txt', 'w') as outfile:  
				json.dump(data_image, outfile)
		self.on.animateClick(10000)
		
                      			

while True:
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
