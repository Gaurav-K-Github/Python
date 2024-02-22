import tkinter as tk
from tkinter import messagebox
import random

def roll_die():
    result = random.randint(1, 6)
    result_label.config(text=f"Die rolled: {result}")

def stop_rolling():
    if messagebox.askyesno("Stop Rolling", "Are you sure you want to stop rolling the die?"):
        root.destroy()

root = tk.Tk()
root.title("Die Roller")

result_label = tk.Label(root, text="Die rolled: ")
result_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Die", command=roll_die)
roll_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Rolling", command=stop_rolling)
stop_button.pack(pady=5)

root.mainloop()
