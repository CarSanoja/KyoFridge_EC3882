
#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
import time
import os
import json
import numpy as np



def sonido_analisis(signal,condicional):
	electret = signal["analogico_1"]
	if condicional == 0:
		pass
	else:
		electret_np = np.asarray(electret)
		hist, bin_edges = np.histogram(electret_np)
		print(np.histogram(electret_np))
		maxi = hist.max()
		maxi_histo = np.asscalar(maxi)
		if maxi_histo > 350: 
			return True
		else:
			return False

#print(sonido_analisis())