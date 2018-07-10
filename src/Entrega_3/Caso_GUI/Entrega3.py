
#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
import serial
import time
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from drawnow import *
import json

# VARIABLES para almacenar los valores de los sensores en el tiempo
signal = {'analogico_1': [],'analogico_2': [],'digital_1': [],'digital_2': []}

# funcion encargada de realizar la lectura y decodificación de una trama nueva
def stream(flag_encabezado = 0):
	#file = open("Generator_data.txt","a")
	# Lectura del puerto serial
	DEMOQE_read.flush()
	while True:
		header = DEMOQE_read.read(1)

		if header[0] == 245:
			read5= True
			print('Encabezado F5 OK!!')
			aux= DEMOQE_read.read(4)
			data_input_2 = header + aux
			break
		elif header[0] == 243:
			read5 = False
			#print('Encabezado F3 OK!!')
			aux = DEMOQE_read.read(2)
			data_input_2 = header + aux
			break
		else:
			print('no encabezado, leyendo otra vez...')
			pass
	#print("KRecepcion nueva completa")
	#print(data_input_2)
	# ETAPA 1: Se verifica que la trama tenga al encabezado siempre de primero
	while True:
		if (read5 == True):
			enc_posi = data_input_2.find(245)
		else:
			enc_posi = data_input_2.find(243)
		
		#print(enc_posi)
		if enc_posi!=0:
			data_input_2 = data_input_2[enc_posi:]
			#print(data_input_2)
			data_input_3 = DEMOQE_read.read(enc_posi)
			#print(data_input_3)
			data_input = data_input_2 + data_input_3
			#print(data_input)
		else:
			data_input = data_input_2
			#print("Aqui estaba bien")
			#print(data_input)
		for datop in data_input_2:
			if read5 == True:
				if datop==245:
					flag_encabezado+=1
			else:
				if datop==243:
					flag_encabezado+=1

		if flag_encabezado>1:
			flag_encabezado=0
			data_input_2 =  b'\x00' + data_input_2[1:]
			#print("Aqui hubo doble encabezado")
		else:
			flag_encabezado = 0
			break
    # ETAPA 2: Decodificación del protocolo
	analogico_1_aux = (((data_input[1] & 31)<<7) + (data_input[2]))*3/4096
	digital_1_aux = (data_input[1] & 64) >> 6  # entrada digital 1
	if read5==True:
		analogico_2_aux = (((data_input[3] & 31)<<7) + (data_input[4]))*3/4096
		digital_2_aux = (data_input[1] & 32) >> 5 # entrada digital 2
		signal["analogico_2"][0] = (analogico_2_aux)
		signal["digital_2"][0] = (digital_2_aux)
	signal["analogico_1"].append(analogico_1_aux)
	signal["digital_1"][0] = (digital_1_aux)
		                    				

DEMOQE_read = serial.Serial('/dev/ttyUSB0',115200)
#plt.ion()
cnt=0
#seg_div = 1
while True:
	stream()
	with open('data.txt', 'w') as outfile:  
		json.dump(signal, outfile)