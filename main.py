from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#40A578"
YELLOW = "#f7f5dd"
YELLOW_1 = "#A1D6B2"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_Sec = WORK_MIN * 60
    short_break_Sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        work_image.config(file="complete.gif")
        title_label.config(text="Rest Break", fg=RED)
        
    elif reps % 2 == 0:
        count_down(short_break_Sec) 
        work_image.config(file="break1.gif")
        title_label.config(text="Break", fg=PINK)
        
    else:
        count_down(work_Sec)
        work_image.config(file="work1.gif")
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60) 
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    
    else: 
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20,pady=30,bg=YELLOW)

title_label = Label(text="Timer",fg="brown" ,bg= YELLOW, font=(FONT_NAME, 30))
title_label.grid(column=1,row=0)
canvas = Canvas(width=348,height=348, bg=YELLOW)
work_image = PhotoImage(file="work1.gif")
canvas.create_image(176,174,image=work_image)
timer_text = canvas.create_text(180,250,text="00:00",fill=YELLOW_1, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()