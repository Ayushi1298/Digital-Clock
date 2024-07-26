from tkinter import *
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("Digital Clock")
root.config(background="black")
def datetime():
    string1=strftime('%H:%M:%S %p')
    label1.config(text=string1)
    label1.after(1000,datetime)
    string2 = strftime('    %A\n %B %d, %Y')
    label2.config(text=string2)

label1=Label(root,font=("digital",70),background="black",foreground="cyan")
label1.pack(anchor='center')
label2=Label(root,font=("digital",32),background="black",foreground="cyan")
label2.pack(anchor='center')
datetime()
root.mainloop()



