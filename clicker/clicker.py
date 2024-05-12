import tkinter as tk
x=0
def xpp():
    global x
    x+=1
    label['text']='Счетчик: {}'.format(x)
root=tk.Tk()
root.title('Кликер')
root.geometry('200x200')
root.resizable(False, False)
button=tk.Button(root,text='ЖМИ', command=xpp)
label=tk.Label(root,text='Счетчик: {}'.format(x))
label_event=tk.Label(root,text='')
label.grid()
button.grid()
label_event.grid()
root.mainloop()
