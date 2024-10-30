import tkinter as tk
from tkinter import messagebox, PhotoImage


def press_key(event):
    if event.char == '\x08':
        clear()
    elif event.char in '+-/*':
        operation(event.char)
    elif event.char == '=':
        calculate()
    elif event.char.isdigit():
        add_digit(event.char)


def clear():
    output['state'] = tk.NORMAL
    output.delete(0, tk.END)
    output.insert(0, '0')
    output['state'] = tk.DISABLED


def calculate():
    value = output.get()
    if value[-1] in '+-/*':  # берем все кроме последнего знака
        value = value + value[:-1]
    output['state'] = tk.NORMAL
    output.delete(0, tk.END)
    try:
        output.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка', 'Деление на 0 невозможно')
        output.insert(0, '0')
    output['state'] = tk.DISABLED


def operation(sign):
    value = output.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = output.get()
    output['state'] = tk.NORMAL
    output.delete(0, tk.END)
    output.insert(0, value + sign)
    output['state'] = tk.DISABLED


def add_digit(digit):
    value = output.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    output['state'] = tk.NORMAL
    output.delete(0, tk.END)
    output.insert(0, value + str(digit))
    output['state'] = tk.DISABLED


def grid_column(index, size):
    win.grid_columnconfigure(index, minsize=size)


def grid_row(index, size):
    win.grid_rowconfigure(index, minsize=size)


def add_digit_button(digit, row_value, column_value):
    button = tk.Button(text=f'{digit}', font=('Arial', 20), bd=7, command=lambda: add_digit(digit))
    button.grid(row=row_value, column=column_value, stick='we ns', padx=10, pady=10)


def add_sign_button(sign, row_value, column_value):
    button = tk.Button(text=sign, font=('Arial', 20), bd=7, command=lambda: operation(sign))
    button.grid(row=row_value, column=column_value, stick='we ns', padx=10, pady=10)


def add_calculate_button(sign, row_value, column_value):
    button = tk.Button(text=sign, font=('Arial', 20), bd=7, command=calculate)
    button.grid(row=row_value, column=column_value, stick='we ns', padx=10, pady=10)


win = tk.Tk()

width = win.winfo_screenwidth()
height = win.winfo_height()

width = width // 2 - 200
height = height // 2 + 250

win.geometry(f'400x500+{width}+{height}')
win.config(bg='#9A9A9A')
win.resizable(False, False)
win.title('Calculator')
icon = PhotoImage(file='calculator_icon.png')
win.iconphoto(False, icon)

output = tk.Entry(win, font=('Arial', 30), width=15, relief=tk.SUNKEN, bd=10)
output.grid(row=0, column=0, columnspan=4, stick='we ns', padx=10, pady=10)
output.insert(0, '0')
output['state'] = tk.DISABLED

win.bind('<Key>', press_key)

# цифры
add_digit_button(1, 1, 0)
add_digit_button(2, 1, 1)
add_digit_button(3, 1, 2)
add_digit_button(4, 2, 0)
add_digit_button(5, 2, 1)
add_digit_button(6, 2, 2)
add_digit_button(7, 3, 0)
add_digit_button(8, 3, 1)
add_digit_button(9, 3, 2)
add_digit_button(0, 4, 0)

# знаки
add_sign_button('+', 1, 3)
add_sign_button('-', 2, 3)
add_sign_button('/', 3, 3)
add_sign_button('*', 4, 3)
add_calculate_button('=', 4, 2)

tk.Button(text='AC', font=('Arial', 20), bd=7, command=clear) \
    .grid(row=4, column=1, stick='we ns', padx=10, pady=10)

# циклы размеры кнопок
for i in range(4):
    grid_column(i, 100)

for i in range(5):
    grid_row(i, 100)

win.mainloop()
