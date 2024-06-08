import tkinter as tk
root = tk.Tk()
root.title("Spinbox Example")
root.geometry("200x100")
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()
root.mainloop()
