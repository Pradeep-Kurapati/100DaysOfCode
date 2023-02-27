from tkinter import *
from random import *
import pandas

# -------------- Constants -------------- #

BACKGROUND_COLOR = "#B1DDC6"
global current_card
# ------------- French Word Generation ---------------- #
data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    print(current_card)
    canvas.itemconfig(background_image, image=my_image_1)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(background_image, image=back_image)


# -------------- Window -------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')
window.config(width=850, height=530)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
my_image_1 = PhotoImage(file='images/card_front.png')
background_image = canvas.create_image(400, 263, image=my_image_1)
canvas.grid(row=1, column=1, columnspan=2)

# Correct button
right_image = PhotoImage(file='images/right.png')
Known_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
Known_button.grid(row=2, column=1)

# Wrong Button
wrong_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
unknown_button.grid(row=2, column=2)

# writing French
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))

# Back Image
back_image = PhotoImage(file='images/card_back.png')

next_word()

window.mainloop()
