
#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
import time
import os
import json
import numpy as np

def sonido_analisis():
	with open('data_im.txt') as json_file:  
			condicional = json.load(json_file)

	with open('data.json') as json_file:  
			signal = json.load(json_file)

	electret = signal["analogico_1"]

	if condicional == 0:
		pass
	else:
		electret_np = np.asarray(electret)
		hist, bin_edges = np.histogram(electret_np)
		print(hist)
		print(hist.max())
		maxi = hist.max()
		maxi_histo = np.asscalar(maxi)
		if maxi_histo > 800: 
			return True
		else:
			return False

print(sonido_analisis())