from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    SECS_IN_MINUTE = 60
    work_session = WORK_MIN * SECS_IN_MINUTE
    short_break_session = SHORT_BREAK_MIN * SECS_IN_MINUTE
    long_break_session = LONG_BREAK_MIN * SECS_IN_MINUTE

    if reps % 8 == 0:
        count_down(long_break_session)
        timer_label.config(text="Break", fg=RED)
        return

    if reps % 2 == 0:
        count_down(short_break_session)
        timer_label.config(text="Break", fg=PINK)
        return


    count_down(work_session)
    timer_label.config(text="Work", fg=GREEN)
    return


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count <= 0:
        return

    window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

check_emoji = "🗿"
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
check_mark.grid(column=1, row=3)


window.mainloop()
