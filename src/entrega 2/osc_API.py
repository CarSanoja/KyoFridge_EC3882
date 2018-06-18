from tkinter import *

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("TUNNING HERE DUDE")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        # create the file object)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        time_base = Menu(menu)
        time_base.add_command(label="0.1 seg / DIV",command=self.caso2)
        time_base.add_command(label="0.02 seg / DIV",command=self.caso3)
        time_base.add_command(label="0.01 seg / DIV",command=self.caso4)
        time_base.add_command(label="0.005 seg / DIV",command=self.caso1)
        #time_base.add_command(label="0.2 seg / DIV",command=self.caso5)
        menu.add_cascade(label="time base", menu=time_base)
        
        Amplitude = Menu(menu)
        Amplitude.add_command(label="0.2 V / DIV",command=self.amplitude1)
        Amplitude.add_command(label="0.5 V / DIV",command=self.amplitude2)
        Amplitude.add_command(label="1 V / DIV",command=self.amplitude3)
        Amplitude.add_command(label="2 V / DIV",command=self.amplitude4)
        menu.add_cascade(label="Amplitud", menu=Amplitude)
        
        Textos = Menu(menu)
        Textos.add_command(label="frecuencia", command=self.Frecuency)
        Textos.add_command(label="Amplitud", command=self.Amplitud)
        Textos.add_command(label="Seg/DIV", command=self.SegDiv)
        Textos.add_command(label="VolDIV", command=self.VolDiv)
        menu.add_cascade(label="Parametros", menu=Textos)
        
    def client_exit(self):
        self.master.destroy()
        
    def caso1(self):
        file = open("time_base_data.txt", "w")
        file.write(str(0.025)) 
    
    def caso2(self):
        file = open("time_base_data.txt", "w")
        file.write(str(0.5)) 
        file.close()
        
    def caso3(self):
        file = open("time_base_data.txt", "w")
        file.write(str(0.1))
        
    def caso4(self):
        file = open("time_base_data.txt", "w")
        file.write(str(0.05))

    def caso5(self):
        file = open("time_base_data.txt", "w")
        file.write(str(1))

        
    def amplitude1(self):
        file = open("amplitud_data.txt", "w")
        file.write(str(2)) 
    
    def amplitude2(self):
        file = open("amplitud_data.txt", "w")
        file.write(str(1)) 
        file.close()
        
    def amplitude3(self):
        file = open("amplitud_data.txt", "w")
        file.write(str(0.5))
        
    def amplitude4(self):
        file = open("amplitud_data.txt", "w")
        file.write(str(0.25))
        
    def Frecuency(self):
        
        text = Label(self, text="Frecuencia = ")
        text.pack()
        
    def Amplitud(self):
        text = Label(self, text="Amplitud pico-pico = ")
        text.pack()
    
    def SegDiv(self):
        file = open("time_base_data.txt","r")
        t = float(file.read())
        if t == 0.025:
            x = "0.005 "
        elif t == 0.5:
            x = "0.1"
        elif t == 0.1:
            x = "0.02"
        elif t == 0.05:
            x = "0.01"
        text = Label(self, text="Segundos por división = "+x)
        text.pack()
    
    def VolDiv(self):
        file = open("amplitud_data.txt","r")
        t = float(file.read())
        if t == 2:
            x = "0.2 "
        elif t == 1:
            x = "0.5"
        elif t == 0.5:
            x = "1"
        elif t == 0.025:
            x = "2"
        text = Label(self, text="Voltaje por división = "+x)
        text.pack()
        
root = Tk()

root.geometry("300x80")

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()