import tkinter as tk

'''функции для кнопок'''
def l1tol2():
    select=list(listbox1.curselection())
    select.reverse()
    listbox2.insert(tk.END,listbox1.get(select))
    listbox1.delete(select)

def l2tol1():
    select=list(listbox2.curselection())
    select.reverse()
    listbox1.insert(tk.END,listbox2.get(select))
    listbox2.delete(select)

def save():
    with open('save1.txt','w') as f:
        f.writelines('список заданных дел:\n')
        f.writelines('\n'.join(listbox1.get(0,tk.END)))
        f.writelines('\n\nсписок выполненных дел:\n')
        f.writelines('\n'.join((listbox2.get(0,tk.END))))

'''создание окна'''
root=tk.Tk()
root.title('программно заданный список дел')
root.geometry('500x500')
root.resizable(False,False)

'''создание виджетов'''
listbox1=tk.Listbox(root)
listbox1.insert(tk.END,'купить молоко','купить кофе','купить чай','выпить чай','выпить кофе','покормить питомца')
listbox2=tk.Listbox(root)
but1=tk.Button(root,text='в список выполненных дел',command=l1tol2)
but2=tk.Button(root,text='в список заданных дел',command=l2tol1)
savebtn=tk.Button(root,text='сохранить',command=save)

'''позиционирование виджетов'''
listbox1.pack()
listbox2.pack()
but1.pack()
but2.pack()
savebtn.pack()

root.mainloop()
