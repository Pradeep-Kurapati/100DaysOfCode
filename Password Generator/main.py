from tkinter import *
import random, string
import pyperclip

#Initialising Window

root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("PASSWORD GENERATOR by Pradeep")

#heading
Label(root, text="PASSWORD GENERATOR", font = "arial 15 bold").pack()
Label(root, text = "Pradeep",font="gothic 15").pack(side=BOTTOM)

#select password length

Label(root, text="Password Length", font="arial 10 bold").pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

#to store password
pass_str = StringVar()
#define function
def Generator():
    password=''
    for x in range(0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password+=random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    pass_str.set(password)

#button
Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

#To copy to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())

#Button
Button(root, text="COPY TO CLIPBOARD", command=Copy_password).pack(pady=5)

#to start the GUI window
root.mainloop()
