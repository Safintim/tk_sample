from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
frame1 = Frame(root, bd=5)
frame2 = Frame(root, bd=5, bg='red')
frame3 = Frame(root, bd=5, bg='green')
frame4 = Frame(root, bd=5, bg='yellow')
# Тройка кнопок
btn1 = Button(frame1, text='Просто кнопка1', bg='white', fg='black')
btn2 = Button(frame1, text='Просто кнопка2', bd=5, bg='yellow', fg='red')
btn3 = Button(frame1, text='Просто кнопка3', bd=2, bg='blue', fg='white')

# label
label1 = Label(
    frame2,
    text='Ниже поля для ввода текста.'
    ' Первая ограниченна одной строкой.'
    ' Вторая сколь угодно',
    font='Times 13 bold italic'
)

# ввод строки
entry1 = Entry(frame2, bd=3)

# ввод текста
text1 = Text(frame2, height=3, wrap=WORD)
text1.insert(1.0, 'Добавить Текст\n в начало первой строки')

# список
values = ['Выбери 1', 'Выбери 2', 'Выбери 3', 'Выбери 4', 'Выбери 5']
listbox1 = Combobox(frame3, values=values)

# checkbutton
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
checkbox1 = Checkbutton(frame3, text='Python', variable=var1, onvalue=1, offvalue=0)
checkbox2 = Checkbutton(frame3, text='Ruby', variable=var2, onvalue=1, offvalue=0)
checkbox3 = Checkbutton(frame3, text='PHP', variable=var3, onvalue=1, offvalue=0)

var = IntVar()
rbutton1 = Radiobutton(frame4, text='100', variable=var, value=1)
rbutton2 = Radiobutton(frame4, text='200', variable=var, value=2)
rbutton3 = Radiobutton(frame4, text='300', variable=var, value=3)

widgets = [
    frame1, frame2, frame3, frame4,
    btn1, btn2, btn3,
    label1, entry1, text1,
    listbox1, checkbox1, checkbox2, checkbox3,
    rbutton1, rbutton2, rbutton3,
]

for widget in widgets:
    widget.pack()


frame1.pack(side='left')
frame2.pack(side='left')
frame3.pack(side='left')
frame4.pack(side='left')
listbox1.pack(side='top')
checkbox1.pack(side='left')
checkbox2.pack(side='left')
checkbox3.pack(side='left')

root.mainloop()
