import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "This is an info message")

root = tk.Tk()
root.title("Messagebox Example")
root.geometry("300x200")

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

root.mainloop()
