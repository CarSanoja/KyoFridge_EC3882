import matplotlib.pyplot as plt

def MakeFig(senal): #Create a function that makes our desired plot
    plt.ylim(100,120)                                 #Set y min and max values
    plt.title('Live Streaming from DemoQE')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Amplitud')                            #Set ylabels
    plt.plot(senal, 'b-', label='Value')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend