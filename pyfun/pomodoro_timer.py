# import time
#
#
# def pomodoro_timer(work_duration=25, short_break=5, long_break=15, cycles=4):
#     for i in range(1, cycles + 1):
#         print(f"\n🍅 Pomodoro {i}: Work for {work_duration} minutes.")
#         countdown(work_duration * 60)
#
#         if i < cycles:
#             print(f"🛀 Take a short break for {short_break} minutes.")
#             countdown(short_break * 60)
#         else:
#             print(f"🎉 All cycles done! Take a long break for {long_break} minutes.")
#             countdown(long_break * 60)
#
#
# def countdown(seconds):
#     while seconds:
#         mins, secs = divmod(seconds, 60)
#         timer = f"{mins:02d}:{secs:02d}"
#         print(f"\r⏰ {timer}", end="")
#         time.sleep(1)
#         seconds -= 1
#     print("\r⏰ 00:00 - Time's up!")
#
#
# if __name__ == "__main__":
#     pomodoro_timer()

import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="pink")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg="green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")

title_label = tk.Label(text="Timer", fg="white", bg="black", font=("Courier", 35))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="black", highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", bg="black", font=("Courier", 20))
check_marks.grid(column=1, row=3)

window.mainloop()