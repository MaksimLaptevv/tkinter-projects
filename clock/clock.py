import tkinter as tk
from time import strftime

root=tk.Tk()
root.title('Часы')
root.geometry('250x50')
root.resizable(False,False)

lable=tk.Label(root,font=('aerial', 30), background='black', foreground='white')
def time():
    string = strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)

lable.pack()
time()
root.mainloop()