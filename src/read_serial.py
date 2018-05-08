#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
# 
import serial
import time
# script that allow to set the graphs for the signal
from graph import *
# Matplotlib to draw functions
import matplotlib.pyplot as plt
# To allow make live data graph we need drawnow
# pip install drawnow
#from drawnow import *


# Opening a Serial port

# - The port is immediately opened on object creation, when a port is given. It is not opened when
# port is None and a successive call to open() is required. port is a device name: depending on 
# operating system. e.g. /dev/ttyUSB0 on GNU/Linux or COM3 on Windows.
# - The parameter baudrate can be one of the standard values:  50, 75, 110, 134, 150, 200, 300, 600, 1200,
# 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200. These are well supported on all platforms.
# - Standard values above 115200, such as:  230400, 460800, 500000, 576000, 921600, 1000000, 1152000,
# 1500000, 2000000, 2500000, 3000000, 3500000, 4000000 also work on many platforms and devices.
# Non-standard values are also supported on some platforms (GNU/Linux, MAC OSX >= Tiger, Windows).
# - Possible values for the parameter timeout which controls the behavior of read():
# .. timeout = None: wait forever until requested number of bytes are received
# .. timeout = 0:  non-blocking mode, return immediately in any case, returning zero or more, up to
# the requested number of bytes
# .. timeout = x:  set timeout to x seconds (float allowed) returns immediately when the requested
# number of bytes are available, otherwise wait until the timeout expires and return all bytes that were
# received until then.
DEMOQE_read = serial.Serial('/dev/ttyACM0',9600,timeout=1);
print(DEMOQE_read.isOpen())
# Set the matplotlib parameters, initializing
plt.ion() # Modo interactivo de matplotlib
input_signal = [] #Entrada al graficador 
while True:
	try:
# To find the Serial port direction we can get the name typing python in the terminal:
# $ python -m serial.tools.list_ports -v
# NOTE: The microcontroller must be connected

# Conditional to check if we have data to receive
		while (DEMOQE_read.inWaiting()==0):
			print("no data") #Wait here until there is data
			pass
# El motivo de utilizar sleep desde es que desde que se crea el objeto Serial hasta que esta disponible
# para ser usado, se necesita un cierto tiempo para abrir el puerto serie. Por tanto, se introduce 
# una espera mediante la funcion Sleep, que pertenece a la libreria time
		time.sleep(1)
		print("voy a leer")
## .readline() help us to read the line sended from the microcontroller.
		data_input = DEMOQE_read.readline()
		print(type(data_input))
		print(data_input[0])
		print(len(data_input))
		#input_value = DEMOQE_read.readline()
		
# print() muestra la linea en la pantalla
		#print(input_value)
# We need float numbers 
		#input_signal.append(float(input_value))
# To close the serial port we introced .close() for the class
		#DEMOQE_read.close()
	except:
		print("Keyboard interrupt")
		break
