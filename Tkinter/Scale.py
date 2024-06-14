import tkinter as tk

root = tk.Tk()
root.title("Scale Example")
root.geometry("300x200")

def print_value(val):
    print(f"Selected value: {val}")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=print_value)
scale.pack()

root.mainloop()
