import numpy as np
from sonido import *
import cv2
from CLAHE import CLAHE
from detect_fruits import main



#Ahora se procede a realizar el sistema de adquisición de imagen
cap = cv2.VideoCapture(0)

while(True):
	# Lo primero es verificar si la señal de análisis fue activado
	SetAnalisis = sonido_analisis()
	print(SetAnalisis)

	#"FRAME BY FRAME"
	ret, frame = cap.read()
	if SetAnalisis==True:
		print("ENTREE")
		cv2.imshow('frame',frame)
		cv2.imwrite('object.png',frame)
		label_out = main()
		print(label_out)
		break
	else:
		pass

	

	# Presionar q para salir
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('object.png',frame)
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
