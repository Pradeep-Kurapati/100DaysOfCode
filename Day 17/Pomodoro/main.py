from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#DA5552"
YELLOW = "#E4B1AB"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
for_reset = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(for_reset)
    timer.config(text='Timer')
    tick.config(text='')
    canvas.itemconfig(counter, text='00:00')
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    if reps % 2 == 0 and reps != 8:
        count_down(WORK_MIN * 60)
        timer.config(text='WORK', fg='#590d22')
    elif reps % 2 == 1:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text='BREAK', fg='#a4133c')
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text='BREAK', fg='#003e1f')
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = floor(count/60)
    count_seconds = count % 60
    if count > 0:
        global for_reset
        for_reset = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔️'
        tick.config(text=marks)

    if count_seconds < 10:
        count_seconds = '0' + str(count_seconds)
    canvas.itemconfig(counter, text=f'{count_min}:{count_seconds}')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
counter = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)

# TIMER #
timer = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(row=1, column=2)

# Start Button
start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=3, column=1)

# Reset button #
reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=3)

# tick mark
tick = Label(fg=GREEN, bg=YELLOW, font=('Arial', 15, 'bold'))
tick.grid(row=5, column=2)


window.mainloop()
