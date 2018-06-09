import serial

DEMOQE_read = serial.Serial('/dev/ttyUSB0',115200)
while True:
	DEMOQE_read.flush()
	data_input_2 = DEMOQE_read.read(5)
	print(data_input_2)
	lista = []
	for x in data_input_2:
		lista.append(x)
	print(lista)