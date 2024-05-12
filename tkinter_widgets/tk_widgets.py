import tkinter as tk
import tkinter.ttk

root=tk.Tk()
root.title('Виджеты tkinter')
root.geometry('500x500')

# Метка (label)
label = tk.Label(root, text='Это Label, метка')
label.pack()

# кнопка (button)
button = tk.Button(root, text='Это Button, кнопка')
button.pack()

# поле ввода (entry)
entry = tk.Entry(root)
entry.insert(0, 'Это поле ввода, entry')
entry.pack()

# флажок (checkbutton)
check = tk.Checkbutton(root, text='Флажок, checkbutton')
check.pack()

# переключатель (radiobutton)
radio = tk.Radiobutton(root, text='Это переключатель, radiobutton')
radio.pack()

# список (listbox)
listbox = tk.Listbox(root)
listbox.insert(0, 'Это список, listbox')
listbox.pack()

# текстовое поле (text)
text = tk.Text(root, height=5, width=20)
text.insert(tk.END, 'Это текстовое поле, text')
text.pack()

# шкала (scale)
scale = tk.Scale(root,from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# combobox
vals = ('option-1','option-2','option-3')
combo = tkinter.ttk.Combobox(root, values=vals)
combo.set('combobox')
combo.pack()

# прогрессбар (progressbar)
progress = tkinter.ttk.Progressbar(root, orient=tk.HORIZONTAL, length=100, mode='indeterminate')
progress.pack()
progress.start(10)

root.mainloop()
