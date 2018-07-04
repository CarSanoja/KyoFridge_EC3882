import numpy as np
from sonido import *
import cv2

# Lo primero es verificar si la señal de análisis fue activado
SetAnalisis = sonido_analisis()

#Ahora se procede a realizar el sistema de adquisición de imagen
cap = cv2.VideoCapture(1)

while(True):
    "FRAME BY FRAME"
    ret, frame = cap.read()
    # Para editar se trabaja sobre los frames
     
    "RESULTADOS"
    cv2.imshow('frame',frame)
    # Presionar q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()