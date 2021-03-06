import sys
from PyQt5 import  QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import QTimer
import numpy as np
import matplotlib.pyplot as plt
import json
import time
from image import *

qtCreatorFile = "dash.ui" # Enter file here.
timer = QTimer()
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.signal = None
		self.data_image = 0
		timer.timeout.connect(self.leer)
		timer.timeout.connect(self.data_temp)
		timer.timeout.connect(self.data_door)
		timer.timeout.connect(self.status_electret)
		timer.timeout.connect(self.take_image)
		timer.start(100)

	def leer(self):
		while True:
			try:
				file = open("testfile.txt","r")
				x = file.read()
				if int(x)==0:
					break
				else:
					pass 
			except:
				break
		#time.sleep(0.005)
		#s=time.time()
		with open('data.json') as json_file:
			self.signal = json.load(json_file)
		#print(time.time() - s )

	def data_temp(self):
		self.temp_grados.setText(str(str(self.signal["analogico_2"])+"°"))
		if  ( 31 <= self.signal["analogico_2"] < 33):
			self.temp_bar.reset()
			self.temp_bar.setValue(66)
			self.temp_suggestion.setText("Take care, it's hot")
			palette = QtGui.QPalette(self.palette())
			palette.setColor(QtGui.QPalette.Highlight,QtGui.QColor(QtCore.Qt.yellow))
			self.temp_bar.setPalette(palette)
		elif (20 <= self.signal["analogico_2"] < 31):
			self.temp_bar.reset()
			self.temp_bar.setValue(33)
			self.temp_suggestion.setText("Temperatura normal")
			palette = QtGui.QPalette(self.palette())
			palette.setColor(QtGui.QPalette.Highlight,QtGui.QColor(QtCore.Qt.green))
			self.temp_bar.setPalette(palette)
		elif ( self.signal["analogico_2"] >= 33):
			self.temp_bar.reset()
			self.temp_bar.setValue(99)
			self.temp_suggestion.setText("Temperatura Alta, llamar al técnico")
			palette = QtGui.QPalette(self.palette())
			palette.setColor(QtGui.QPalette.Highlight,QtGui.QColor(QtCore.Qt.red))
			self.temp_bar.setPalette(palette)

	def data_door(self):
		if self.signal["digital_1"] == 1:
			self.door_status.setText(str("Puerta Abierta"))	
		else:
			self.door_status.setText(str("Puerta Cerrada"))

	def take_image(self):
		if self.data_image == 1:
			label = image_capture(self.signal,self.data_image)
			#print(label)
			#print("escribir label")
			if label != None:
				self.nevera_result.setText(str(label))
			else:
				pass
		else:
			pass

	def status_electret(self):
		if self.signal["digital_2"] == 1:
			self.electret_enable.setText(str("Esperando comando de voz"))
			#print("FUUUCCCKKKKK")
			self.data_image = 1
			#print("ya me voy")
		else:
			self.electret_enable.setText(str(" No Escuchando "))
			self.data_image = 0

while True:
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
