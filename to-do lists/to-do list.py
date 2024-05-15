import tkinter as tk

'''функции для кнопок'''
def addition():
    todoList.insert(tk.END, entry.get())
    entry.delete(0,tk.END)

def delete():
    select=list(todoList.curselection())
    select.reverse()
    for i in select:
        todoList.delete(i)

def delete_all():
    todoList.delete(0,tk.END)

def save():
    with open('save.txt','w') as f:
        f.writelines('\n'.join(todoList.get(0,tk.END)))
    todoList.delete(0,tk.END)

'''создание окна'''
root=tk.Tk()
root.title('Список дел')
root.geometry('300x325')
root.resizable(False,False)

'''создание нужных виджетов'''
todoList=tk.Listbox(root)
entry=tk.Entry(root)
entry.insert(0,'список дел:')
add_button=tk.Button(root,text='добавить',command=addition)
save_button=tk.Button(root,text='сохранить',command=save)
delete_button=tk.Button(root,text='удалить',command=delete)
deleteALL_button=tk.Button(root,text='удалить все',command=delete_all)

'''позиционируем виджеты на окне'''
todoList.pack()
entry.pack()
add_button.pack()
save_button.pack()
delete_button.pack()
deleteALL_button.pack()

root.mainloop()