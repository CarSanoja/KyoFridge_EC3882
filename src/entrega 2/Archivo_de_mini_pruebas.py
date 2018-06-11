import serial

DEMOQE_read = serial.Serial('/dev/ttyUSB0',115200)
flag_encabezado = 0
while True:
	DEMOQE_read.flush()
	data_input_2 = DEMOQE_read.read(5)
	print("INICIAAANDOOOOOOOO")
	print(data_input_2)
	print(len(data_input_2))
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
			print("sobreescribo data_input, encabezado corregido")
		else:
			data_input = data_input_2
			print("Sobreescribo data_input, encabezado ok")
			#print("Aqui estaba bien")
			#print(data_input)
		for datop in data_input:
			if datop==245:
				print("encabezado se hace 1")
				flag_encabezado+=1

		if flag_encabezado>1:
			flag_encabezado=0
			data_input_2 =  b'\x00' + data_input_2[1:]
			print("dummy")
			#print("Aqui hubo doble encabezado")
			#print(data_input_2)
		else:
			flag_encabezado = 0
			break
	print(data_input)
	print(len(data_input))
	analogico_1_aux = (((data_input[1] & 31)<<7) + (data_input[2]))
	print(data_input[1])
	print(data_input[2])
	print(analogico_1_aux)