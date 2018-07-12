import numpy as np
from sonido import *
import cv2
from CLAHE import CLAHE
from detect_fruits import main


def image_capture(signal,condicional):

	#Ahora se procede a realizar el sistema de adquisición de imagen
	cap = cv2.VideoCapture(1)
		# Lo primero es verificar si la señal de análisis fue activado
	SetAnalisis = sonido_analisis(signal,condicional)
	print(SetAnalisis)
	if SetAnalisis==False:
		ret, frame = cap.read()
		#print("ENTREE")
		cv2.imshow('frame',frame)
		cv2.imwrite('object.png',frame)
		#print("Entrando a detect fruit")
		try:
			label_out = main()
		except:
			cap.release()
			cv2.destroyAllWindows()
			return None
		#print(label_out)
		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()
		return(label_out)
	else:
		return None


