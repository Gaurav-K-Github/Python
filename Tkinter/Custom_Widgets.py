import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self["bg"] = "yellow"
        self["fg"] = "red"

root = tk.Tk()
root.title("Custom Widget Example")
root.geometry("300x200")

button = CustomButton(root, text="Custom Button")
button.pack(pady=20)

root.mainloop()
