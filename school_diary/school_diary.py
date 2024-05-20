import tkinter as tk

root = tk.Tk()
root.title('дневник')
root.geometry('400x880')
root.resizable(False, False)
students_dict = dict()

def delete_empty(name):
    for i in students_dict[name]:
        try:
            int(i)
        except ValueError:
            students_dict[name].remove(i)

def examination_name(name_student):
    if students_dict.__contains__(name_student):
        return True
    else:
        return False

def examination(name_student):
    if examination_name(name_student) is False:
        return False
    list_marks = students_dict[name_student]
    sum = 0
    for i in list_marks:
        try:
            sum += int(i)
        except ValueError:
            return False
    return True

def add_name_and_marks():
    name = ent_name_add.get()
    if name.strip() == '':
        label_err['text'] = 'Имя ученика не должно быть пустым!'
        ent_name_add.delete(0, tk.END)
        ent_marks.delete(0, tk.END)
    elif students_dict.__contains__(name):
        label_err['text'] = 'Этот пользователь уже существует!'
        label_err.pack()
        ent_name_add.delete(0, tk.END)
        ent_marks.delete(0, tk.END)
    else:
        if label_err['text'] != '':
            label_err['text'] = ''
        marks_list = ent_marks.get().split(',')
        students_dict[name] = marks_list
        delete_empty(name)
        ent_marks.delete(0, tk.END)
        ent_name_add.delete(0, tk.END)

def get_data():
    name = ent_name_get.get()
    ent_name_get.delete(0, tk.END)
    if examination(name) is True:
        marks_sum = 0
        str_marks = ''
        str_marks_new = ''
        for el in students_dict[name]:
            el_for_str = el + ', '
            str_marks += el_for_str
            marks_sum += int(el)
        for i in range(len(str_marks) - 2):
            str_marks_new += str_marks[i]
        if students_dict[name] != []:
            label_all_marks['text'] = 'Оценки ученика: {}'.format(str_marks_new)
            gpa = marks_sum / len(students_dict[name])
            label_gpa['text'] = 'Средний балл ученика: {}'.format(gpa)
        else:
            label_all_marks['text'] = 'У ученика нет оценок'
            label_gpa['text'] = ''
    else:
        label_all_marks['text'] = 'У ученка нет оценок! / Неправильный ввод имени!'
        label_gpa['text'] = ''

def add_marks():
    name = ent_name_change.get()
    bool_ex = examination_name(name)
    if bool_ex is True:
        ent_name_change.delete(0, tk.END)
        marks_str = ent_marks_change.get()
        ent_marks_change.delete(0, tk.END)
        marks_list = marks_str.split(',')
        for i in marks_list:
            students_dict[name].append(i)
        delete_empty(name)
    else:
        label_err_ch['text'] = 'Неправильный ввод имени'

def delete_by_name():
    name = ent_name_del.get()
    ent_name_del.delete(0, tk.END)
    if examination_name(name) is True:
        students_dict.pop(name)
        label_status['text'] = '{} - успешно удален!'.format(name)
    else:
        label_status['text'] = 'Неправильный ввод имени'
def save_txt():
    with open('../../PycharmProjects/pythonProject1/.venv/saved.txt', 'w') as file:
        for key, val in students_dict.items():
            file.write('{} - {}\n'.format(key, val))

label_delimiter = tk.Label(root, text='________________________________________________________________________')
label_delimiter2 = tk.Label(root, text='________________________________________________________________________')
label_delimiter3 = tk.Label(root, text='________________________________________________________________________')
label_delimiter4 = tk.Label(root, text='________________________________________________________________________')


label_add_student = tk.Label(root, text='Добавить ученика:\n')
label_ent_name_add = tk.Label(root, text='Введите имя ученика')
ent_name_add = tk.Entry(root)
label_ent_marks = tk.Label(root, text='Введите оценки ученика')
ent_marks = tk.Entry(root)
button_add = tk.Button(root, text='Добавить ученика', command=add_name_and_marks)
label_err = tk.Label(root, text='')


label_get_student = tk.Label(root, text='\nОценки ученика:\n')
label_ent_name_get = tk.Label(root, text='Введите имя ученика')
ent_name_get = tk.Entry(root)
button_ent_name = tk.Button(root, text='Ввести имя', command=get_data)
label_all_marks = tk.Label(root, text='')
label_gpa = tk.Label(root, text='')


label_rename = tk.Label(root, text='\nИзменить оценки ученика\n')
label_ent_name_change = tk.Label(root, text='Введите имя:')
ent_name_change = tk.Entry(root)
label_ent_marks_change = tk.Label(root, text='Введите оценку(и)')
ent_marks_change = tk.Entry(root)
button_add_marks = tk.Button(root, text='Добавить оценку(и)', command=add_marks)
label_err_ch = tk.Label(root, text='')


label_del = tk.Label(root, text='\nУдалить ученика\n')
label_del_name = tk.Label(root, text='Введите имя:')
ent_name_del = tk.Entry(root)
but_del = tk.Button(root, text='Удалить', command=delete_by_name)
label_status = tk.Label(root, text='')


label_save = tk.Label(root, text='\nСохранить как...\n')
but_save_txt = tk.Button(root, text='.txt', command=save_txt)

label_add_student.pack()
label_ent_name_add.pack()
ent_name_add.pack()
label_ent_marks.pack()
ent_marks.pack()
button_add.pack()
label_err.pack()
label_delimiter.pack()


label_get_student.pack()
label_ent_name_get.pack()
ent_name_get.pack()
button_ent_name.pack()
label_all_marks.pack()
label_gpa.pack()


label_delimiter2.pack()
label_rename.pack()
label_ent_name_change.pack()
ent_name_change.pack()
label_ent_marks_change.pack()
ent_marks_change.pack()
button_add_marks.pack()
label_err_ch.pack()


label_delimiter3.pack()
label_del.pack()
label_del_name.pack()
ent_name_del.pack()
but_del.pack()
label_status.pack()


label_delimiter4.pack()
label_save.pack()
but_save_txt.pack()


root.mainloop()
