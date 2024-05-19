from tkinter import *
import PIL
from PIL import ImageTk, Image
root = Tk()
root.geometry('900x600+510+240')


def button_click1():
    global numb
    numb = 1
    check()


def button_click2():
    global numb
    numb = 2
    check()


def button_click3():
    global numb
    numb = 3
    check()


def button_click4():
    global numb
    numb = 4
    check()


def check():
    global score, q
    if check_answ[q - 1] == str(numb):
        score += 1
    if q < numb_question:
        q += 1
        question_label.configure(text=question[q - 1])
        answ1_label.configure(text=answ1[q - 1])
        answ2_label.configure(text=answ2[q - 1])
        answ3_label.configure(text=answ3[q - 1])
        answ4_label.configure(text=answ4[q - 1])
    else:
        question_label.destroy()
        answ1_label.destroy()
        answ2_label.destroy()
        answ3_label.destroy()
        answ4_label.destroy()
        text = f'Вы ответили правильно на {score} вопросов из {numb_question}'
        result_label.configure(text=text)
        result_label.configure(state='normal')
        button_restart.configure(state='normal')


def create():
    global question_label, answ1_label, answ2_label, answ3_label, answ4_label, result_label,  button_restart

    result_label = Label(root, text='', font='Segoe 26', anchor='center', wraplength=400, justify='center')
    result_label.place(x=20, y=100, width=400, height=100)
    result_label.configure(state='disabled')
    button_restart = Button(root, text='Пройти снова', bg='#6495ED', font='Times 14', anchor='w', command=start)
    button_restart.place(x=20, y=440, width=300, height=60)
    button_restart.configure(state='disabled')

    question_label = Label(root, text=question[q - 1], bg='#6495ED', font='Times 14', anchor='w', wraplength=400)
    question_label.place(x=20, y=100, width=400, height=100)

    answ1_label = Button(root, text=answ1[q - 1], bg='#6495ED',
                         font='Times 14', anchor='w', command=button_click1)
    answ1_label.place(x=20, y=230, width=300, height=60)

    answ2_label = Button(root, text=answ2[q - 1], bg='#6495ED',
                         font='Times 14', anchor='w', command=button_click2)
    answ2_label.place(x=20, y=300, width=300, height=60)

    answ3_label = Button(root, text=answ3[q - 1], bg='#6495ED',
                         font='Times 14', anchor='w', command=button_click3)
    answ3_label.place(x=20, y=370, width=300, height=60)

    answ4_label = Button(root, text=answ4[q - 1], bg='#6495ED',
                         font='Times 14', anchor='w', command=button_click4)
    answ4_label.place(x=20, y=440, width=300, height=60)



def start():
    global data, question, answ1, answ2, answ3, answ4, check_answ, numb_question, q, numb, score, icon, img
    data = []
    with open('params.txt', mode='r', encoding='UTF-8') as file:
        for line in file.readlines():
            data.append(line.strip())

    root.title(data[0])
    icon = PhotoImage(file=data[1])
    root.iconphoto(True, icon)

    question = []
    answ1 = []
    answ2 = []
    answ3 = []
    answ4 = []
    check_answ = []

    numb_question = (len(data) - 3)//6

    img = Image.open(data[1])
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)
    image = Label(root, image=img)
    image.place(width=400, height=400, x=500, y=100)

    for i in range(3, 6*numb_question+3, 6):
        question.append(data[i])
        answ1.append(data[i + 1])
        answ2.append(data[i + 2])
        answ3.append(data[i + 3])
        answ4.append(data[i + 4])
        check_answ.append(data[i + 5])

    numb = 0
    q = 1
    score = 0
    create()

start()

root.mainloop()
