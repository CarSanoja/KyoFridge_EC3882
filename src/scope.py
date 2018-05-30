import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2
#from prueba_opencv import *

def nothing():
    pass 

class Scope(object):
    def __init__(self, ax, maxt=0.2, dt=0.001):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 4000)
        self.ax.set_xlim(0, self.maxt)

    def update(self, i):
        lastt = self.tdata[-1]
        file2 = open("time_base_data.txt","r")
        t2_read = float(file2.read())
        self.maxt = t2_read
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        y = int(file_splitted[i])
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,


def emitter():
    i = 0
    while i <= len_file:
        i += 1
        yield i

file = open("Generator_data.txt","r")
file_read = file.read()
file_splitted = file_read.split("\n")
len_file = len(file_splitted)

fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=10,
                              blit=True)
plt.grid()
plt.show()

    