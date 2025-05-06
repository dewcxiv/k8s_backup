import tkinter as tk
import random

affirmations = [
    "You are beautiful inside and out💕",
    "The love I seek is seeking me too 💞🔓💫",
    "You radiate confidence and love✨",
    "I speak and move with clarity and courage 💪",
    "Love flows to me effortlessly and naturally 🧲💘🌠",
    "You are worthy of all your dreams💖",
    "Your energy is pure magic🌟",
    "My presence is powerful and magnetic 🌟🧲💃",
    "I deserve a love that is kind, passionate, and lasting ❤️👁️🌹",
    "I am becoming the best version of myself, one step at a time 👑",
    "With every breath, I call in the love that aligns with my soul 🌬️💞",
    "You light up every room you enter🌷",
    "You are growing and glowing, girl!🌸",
    "You deserve kindness - especially from yourself💞",
    "Slay today with your soft power👑",
    "I attract relationships that nourish and uplift me 👫🌷🌞",
    "I trust myself and my intuition. 🌙🧘‍♀️🔮"
]

def show_affirmation():
    message = random.choice(affirmations)
    text_label.config(text=message)

window = tk.Tk()
window.title("Daily Glow-up 💅 Affirmation")
window.config(padx=30, pady=30, bg="#FFDDEE")\

title = tk.Label(text="Hey beautiful, click for a boost 💖", font=("Helvetica", 16, "bold"), bg="#FFDDEE", fg="#C71585")
title.pack(pady=10)

text_label = tk.Label(text="", font=("Helvetica", 14), wraplength=300, bg="#FFDDEE", fg="#8B008B", justify="center")
text_label.pack(pady=20)

button = tk.Button(text="Give me love 💘", command=show_affirmation, font=("Helvetica", 12), bg="#FFB6C1", fg="white", padx=10, pady=5)
button.pack()

window.mainloop()