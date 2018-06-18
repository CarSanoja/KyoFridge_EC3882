
#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
import serial
import time
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from drawnow import *


# VARIABLES para almacenar los valores de los sensores en el tiempo
signal = {'analogico_1': [],'analogico_2': [],'digital_1': [],'digital_2': []}

# funcion encargada de realizar la lectura y decodificación de una trama nueva
def stream(flag_encabezado = 0):
	#file = open("Generator_data.txt","a")
	# Lectura del puerto serial
	DEMOQE_read.flush()
	data_input_2 = DEMOQE_read.read(5)
	#print("KRecepcion nueva completa")
	#print(data_input_2)
	# ETAPA 1: Se verifica que la trama tenga al encabezado siempre de primero
	while True:
		enc_posi = data_input_2.find(245)
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
			if datop==245:
				flag_encabezado+=1
		if flag_encabezado>1:
			flag_encabezado=0
			data_input_2 =  b'\x00' + data_input_2[1:]
			#print("Aqui hubo doble encabezado")
			#print(data_input_2)
		else:
			flag_encabezado = 0
			break

	#print("Aqui ya salio del while la trama bien")
	#print(data_input)
    # ETAPA 2: Decodificación del protocolo
	analogico_1_aux = (((data_input[1] & 31)<<7) + (data_input[2]))
	signal["analogico_1"].append(analogico_1_aux)

def makeFig():
	# Se verifica la base de tiempo a imprimir como osciloscopio
	file2 = open("time_base_data.txt","r")
	t2_read = float(file2.read())
	plt.ylim(0,4200) 
	plt.title('My Live Streaming Sensor Data')
	plt.grid(True)                                  			
	plt.ylabel('Pablonski temp')    
	plt.xlim(0, t2_read)                       			
	plt.plot([t*0.0005 for t in range(0,200, 1)],signal["analogico_1"][len(signal["analogico_1"])-200:], 'r-', label='Electret')        
	plt.legend(loc='upper left')                    				

# DEMOQE_read = serial.Serial('/dev/ttyUSB4',115200) #linux
DEMOQE_read = serial.Serial('COM3',115200) # windows 
plt.ion()
cnt=0
#seg_div = 1
while True:
	stream()
	cnt=cnt+1
	if cnt == 200:
		drawnow(makeFig)                       #Call drawnow to update our live graph
		plt.pause(.000001)
		signal["analogico_1"]
		cnt = 0                     #Pause Briefly. Important to keep drawnow from crashing
	print(signal["analogico_1"][len(signal["analogico_1"])-1])

