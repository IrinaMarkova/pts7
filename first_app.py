import tkinter
from tkinter import messagebox


def button_click():
    messagebox.showinfo(title='Информация', message='ты нажал на кнопку')

# --- создание основного окна ---
root = tkinter.Tk()
root.geometry('400x290')
# --- создание заголовка---
root.title('мое приложение')


# --- создание надписей ---
label = tkinter.Label(root, text= 'меня зовут Ира', font=('Arial', 18), fg='pink')
label.pack()

# --- Создание кнопки ---
button = tkinter.Button(root, text='жать сюда', command=button_click)
button.pack()

# --- запуск основного цикла ---
root.mainloop()



