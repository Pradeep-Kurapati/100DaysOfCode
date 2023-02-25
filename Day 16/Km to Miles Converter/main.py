from tkinter import *


def calculate():
    km = float(input_for_form.get())
    mile = round(km * 1.609, 2)
    answer_label.config(text=f'{mile}')

# Specifying Window


window = Tk()
window.minsize(width=300, height=80)
window.config(padx=20, pady=20)
window.title('Km To Mile Converter')

# Specifying Input
input_for_form = Entry(width=7)
input_for_form.grid(row=5, column=5)

# Specifying Miles
miles = Label(text='Miles')
miles.grid(row=5, column=8)

# Specifying text
is_equal = Label(text='is equal to ')
is_equal.grid(row=7, column=3)

# Specifying Answer
answer_label = Label(text='0')
answer_label.grid(row=7, column=5)

# Specifying KM Label
kilo = Label(text='KM')
kilo.grid(row=7, column=7)

# Specifying Button
calci = Button(text='calculate', command=calculate)
calci.grid(row=8, column=5)

window.mainloop()
