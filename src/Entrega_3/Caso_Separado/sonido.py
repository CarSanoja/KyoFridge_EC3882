
#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
import time
import os
import json
import numpy as np

def sonido_analisis():
	with open('data_im.txt') as json_file:  
			condicional = json.load(json_file)

	with open('data.txt') as json_file:  
			signal = json.load(json_file)

	electret = signal["analogico_1"][len(signal["analogico_1"])-400:]

	if condicional == 0:
		pass
	else:
		electret_np = np.asarray(electret)
		suma_data = electret_np.sum()
		if suma_data > 800:
			return True
		else:
			return False