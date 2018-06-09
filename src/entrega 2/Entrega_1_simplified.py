
#The libraries we are going to use are PySerial and Time
# PySerial is encapsulates the access for the serial port.
import serial
import time
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


# In[76]:


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


# In[111]:


# VARIABLES para almacenar los valores de los sensores en el tiempo
#digital_1 = []
#digital_2 = []
signal = {'analogico_1': [],'analogico_2': [],'digital_1': [],'digital_2': []}
#analogico_1 = []
#signal["analogico_1"].append(0)
#analogico_2 = []
# Constantes de manipulacion para el main
flag_first_run = 0
flag_trama_len_cst = 0
list_pos_trama = []
i = 0
j = 0
data_list = []
#os.remove("Generator_data.txt")
file = open("Generator_data.txt","w")
file.write("0")
file.close()

#Hex to binary
def dec_to_bin(dec):
	dec_str = str(int(dec))
	cod_bin = bin(int(dec_str))
	return cod_bin

#Binary to decimal
def bin_to_dec(bina):
	cod_dec = int(str(bina),2)
	return cod_dec

# This function make possible to split an integer number to separate the information we want.
# First we have to translate the hexa code to binary. Second we save every bit following the
# protocol order:
# 0 D1 D2 A11 A10 A9 A8 A7
def decode_channel1_one(number):
    #decode Channel one
	part_one_bin = dec_to_bin(number)
	len_bit_number = len(part_one_bin) -2
	diferencia = 8 - len_bit_number
	cero_faltante = "0"*diferencia
	part_one_bin_comp = (cero_faltante + str(part_one_bin[2:]))
	digital_one = part_one_bin_comp[1]
	digital_two = part_one_bin_comp[2]
	analogic_most_significant = part_one_bin_comp[3:]
	return digital_one,digital_two,str(analogic_most_significant)


# In[115]:


# This function make possible to split an integer number to separate the information we want.
# First we have to translate the hexa code to binary. Second we save every bit following the
# protocol order:
# 0 A6 A5 A4 A3 A2 A1 A0
def decode_channel12_two(number):
    #decode channe one and two for less significant bits
	part_one_bin = dec_to_bin(number)
	len_bit_number = len(part_one_bin) -2
	diferencia = 8 - len_bit_number
	cero_faltante = "0"*diferencia
	part_one_bin_comp = (cero_faltante + str(part_one_bin[2:]))
	analogic_less_significant = part_one_bin_comp[1:]
	return str(analogic_less_significant)


# In[116]:


# This function make possible to split an integer number to separate the information we want.
# First we have to translate the hexa code to binary. Second we save every bit following the
# protocol order:
# 0 0 0 A11 A10 A9 A8 A7
def decode_channel2_one(number):
    # decode channel two for most significant bits
	part_one_bin = dec_to_bin(number)
	len_bit_number = len(part_one_bin) -2
	diferencia = 8 - len_bit_number
	cero_faltante = "0"*diferencia
	part_one_bin_comp = (cero_faltante + str(part_one_bin[2:]))
	analogic_most_significant = part_one_bin_comp[3:]
    
	return str(analogic_most_significant)


# In[117]:


# We need to concatened the entirely analogic information.
def concatenation(string1,string2):
	return bin_to_dec(int(string1 + str(string2)))


def stream(flag_encabezado = 0):
	#file = open("Generator_data.txt","a")
	DEMOQE_read.flush()
	data_input_2 = DEMOQE_read.read(5)
	print("KRecepcion nueva completa")
	print(data_input_2)
	while True:
		enc_posi = data_input_2.find(245)
		print(enc_posi)
		if enc_posi!=0:
			data_input_2 = data_input_2[enc_posi:]
			print(data_input_2)
			data_input_3 = DEMOQE_read.read(enc_posi)
			print(data_input_3)
			data_input = data_input_2 + data_input_3
			print(data_input)
		else:
			data_input = data_input_2
			print("Aqui estaba bien")
			print(data_input)
		for datop in data_input_2:
			if datop==245:
				flag_encabezado+=1
		if flag_encabezado>1:
			flag_encabezado=0
			data_input_2 =  b'\x00' + data_input_2[1:]
			print("Aqui hubo doble encabezado")
			print(data_input_2)
		else:
			break
	data_list.append(data_input)
	print("Aqui ya salio del while la trama bien")
	print(data_input)
    #Decodificacion
	analogico_1_aux = (((data_input[1] & 31) << 7) + data_input[2])/2**12
	print(analogico_1_aux)
	signal["analogico_1"].append(analogico_1_aux)


def nothing():
	pass 

class Scope(object):
	def __init__(self, ax, maxt=0.5, dt=0.001):
		self.ax = ax
		self.dt = dt
		self.maxt = maxt
		self.tdata = [0]
		self.ydata = [0]
		self.line = Line2D(self.tdata, self.ydata)
		self.ax.add_line(self.line)
		self.ax.set_ylim(0, 2)
		self.ax.set_xlim(0, self.maxt)
		self.len_ana1_aux = 1
		self.Amplitude = 1
	def update(self, i):
		lastt = self.tdata[-1]
        #print(datos_analogico_1)
		self.len_ana1_aux = len(signal["analogico_1"])
		file2 = open("time_base_data.txt","r")
		t2_read = float(file2.read())
		file3 = open("amplitud_data.txt","r")
		self.Amplitude = float(file3.read())
		self.maxt = t2_read
		self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
		if lastt > self.tdata[0] + self.maxt:  # reset the arrays
			self.tdata = [self.tdata[-1]]
			self.ydata = [self.ydata[-1]]
			self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
			self.ax.figure.canvas.draw()
		t = self.tdata[-1] + self.dt
		self.tdata.append(t)
		y = (float(signal["analogico_1"][len(signal["analogico_1"])-1])*3/4095)*self.Amplitude
		self.ydata.append(y)
		self.ax.set_ylim(0, 2)
		self.line.set_data(self.tdata, self.ydata)
		file.close()
		file2.close()
		return self.line,

fig, ax = plt.subplots()

while True:
	DEMOQE_read = serial.Serial('/dev/ttyUSB0',115200)
	scope = Scope(ax)
	ani = animation.FuncAnimation(fig, scope.update, interval=10,blit=True)
	stream()
	plt.show(block=False)
	plt.pause(0.001)
	DEMOQE_read.close()

