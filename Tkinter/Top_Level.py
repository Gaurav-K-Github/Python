import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text="This is a new window")
    label.pack()

root = tk.Tk()
root.title("Toplevel Example")
root.geometry("300x200")

button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack()

root.mainloop()
