from tkinter import *

window = Tk()
window.title('My First GUI program.')
window.minsize(width=500, height=300)

# Label
my_label = Label(text='I Am a Label.', font=('Arial', 24, 'normal'))
my_label.grid(row=0, column=0)

# Button


def button_clicked():
    my_label['text'] = form.get()


button = Button(text='Click Me!', command=button_clicked)
button.grid(row=1, column=1)

# Input
form = Entry(width=15)
form.grid(row=2, column=2)


# New button
new_button = Button(text='New Button')
new_button.grid(row=0, column=2)

window.mainloop()
