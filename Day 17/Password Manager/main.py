from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    letters_in_password = [random.choice(letters) for _ in range(nr_letters)]

    symbols_in_password = [random.choice(symbols) for _ in range(nr_symbols)]

    numbers_in_password = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_in_password + symbols_in_password + numbers_in_password

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    email_to_add = user_name.get()
    website_to_add = website_name.get()
    password_to_add = password_entry.get()

    if len(website_to_add) == 0 or len(password_to_add) == 0:
        messagebox.showerror(title='Error!', message='Please Enter all fields.')
    else:
        is_ok = messagebox.askokcancel(title=website_to_add,
                                       message=f'You entered:\nWebsite: {website_to_add}\nPassword: {password_to_add}')

        if is_ok:
            text_to_add = f'{email_to_add} | {website_to_add} | {password_to_add}\n'
            with open('data.txt', mode='a') as file:
                file.write(text_to_add)
                website_name.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=2)

# Website Label
website_label = Label(text='Website')
website_label.grid(row=2, column=1)
website_name = Entry(width=45)
website_name.grid(row=2, column=2, columnspan=2)
website_name.focus()

# Email Label
user_label = Label(text='Email/Username')
user_label.grid(row=3, column=1)
user_name = Entry(width=45)
user_name.grid(row=3, column=2, columnspan=2)
user_name.insert(END, "kurapatipradeep0@gmail.com")

# Password Label
password_label = Label(text='Password')
password_label.grid(row=4, column=1)
password_entry = Entry(width=26)
password_entry.grid(row=4, column=2)

# Generate Password Button
generate = Button(text='Generate Password', width=14, command=generate_password)
generate.grid(row=4, column=3)

# Add Button
add = Button(text='Add', width=45, command=save)
add.grid(row=5, column=2, columnspan=2)

window.mainloop()
