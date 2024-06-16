import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()
root.title("Color Picker Example")
root.geometry("300x200")
def choose_color():
 color_code = colorchooser.askcolor(title="Choose a color")
 print(color_code)
button = tk.Button(root, text="Pick a Color", command=choose_color)
button.pack()
root.mainloop()
