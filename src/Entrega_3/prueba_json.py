
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

with open('data.txt', 'w') as outfile:  
    json.dump(signal, outfile)