from autocorrect import Speller # pip install autocorrect
import tkinter as tk # pip install tkinter

def correct():
    str=entry.get()
    entry.delete(0,tk.END)
    spell=Speller('ru')
    label['text']=spell(str)

root=tk.Tk()
root.geometry('400x200')
root.title('проверка текста')

entry=tk.Entry(root)
button=tk.Button(root,text='enter',command=correct)
label=tk.Label(root,text='Тут будет исправленный текст')

entry.pack()
button.pack()
label.pack()

root.mainloop()