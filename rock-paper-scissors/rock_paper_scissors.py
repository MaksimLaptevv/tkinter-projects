import tkinter as tk
import random

wins = 0
loss = 0
draws = 0

def game(x):
    list_rpc = ['камень',
                'ножницы',
                'бумага']                    # Логика:
    computer = random.choice(list_rpc)       # камень бьет ножницы | ножницы бьют бумагу | бумага бьет камень
    player = list_rpc[x]

    global wins
    global loss
    global draws

    if computer is list_rpc[0]:
        computer_lable['text'] = 'Компьютер выбрал - {}'.format(list_rpc[0])

        if player is list_rpc[0]:

            draws += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[0])
            wl['text'] = 'Ничьих - {}'.format(draws)

        elif player is list_rpc[1]:

            loss += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[1])
            ll['text'] = 'Пройгрышей - {}'.format(loss)

        else:

            wins += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[2])
            dl['text'] = 'Побед - {}'.format(wins)

    elif computer is list_rpc[1]:
        computer_lable['text'] = 'Компьютер выбрал - {}'.format(list_rpc[1])

        if player is list_rpc[0]:

            wins += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[0])
            dl['text'] = 'Побед - {}'.format(wins)

        elif player is list_rpc[1]:

            draws += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[1])
            wl['text'] = 'Ничьих - {}'.format(draws)

        else:

            loss += 1
            computer_lable['text'] = 'Компьютер выбрал - {}'.format(list_rpc[1])
            ll['text'] = 'Пройгрышей - {}'.format(loss)

    else:
        computer_lable['text'] = 'Компьютер выбрал - {}'.format(list_rpc[2])

        if player is list_rpc[0]:

            loss += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[0])
            ll['text'] = 'Пройгрышей - {}'.format(loss)

        elif player is list_rpc[1]:

            wins += 1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[1])
            dl['text'] = 'Побед - {}'.format(wins)

        else:

            draws+=1
            player_lable['text'] = 'Ты выбрал - {}'.format(list_rpc[2])
            wl['text'] = 'Ничьих - {}'.format(draws)

root = tk.Tk()
root.title('Камень ножницы бумага')
root.geometry('400x250')
root.resizable(False,False)

rock = tk.Button(root,text='камень ✊',command=lambda x=0: game(x))
scissors = tk.Button(root,text='ножницы ✌️',command=lambda x=1: game(x))
paper = tk.Button(root,text='бумага ✋', command=lambda x=2: game(x))

wl = tk.Label(root,text='Ничьих - {}'.format(draws))
ll = tk.Label(root,text='Пройгрышей - {}'.format(loss))
dl = tk.Label(root,text='Побед - {}'.format(wins))

lable=tk.Label(root,text='_____________')
lable1=tk.Label(root,text="____________")

computer_lable = tk.Label(root, text='Компьютер выбрал - {}'.format('пока что тут пусто'))
player_lable = tk.Label(root, text='Ты выбрал - {}'.format('пока что тут пусто'))

rock.pack()
scissors.pack()
paper.pack()

lable.pack()

wl.pack()
ll.pack()
dl.pack()

lable1.pack()

computer_lable.pack()
player_lable.pack()

root.mainloop()