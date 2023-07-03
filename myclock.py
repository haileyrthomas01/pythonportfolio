from tkinter import *
from time import strftime

myWindow = Tk();
myWindow.title('My Clock')

def time() :
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindow, font = ('arial', 40, 'bold'),
              background= 'light blue', 
              foreground= 'white')

clock.pack(anchor= 'center')
time()

mainloop()