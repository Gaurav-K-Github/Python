import tkinter as tk
from tkinter.ttk import Notebook

root = tk.Tk()
root.title("Notebook Example")
root.geometry("400x300")

notebook = Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

label1 = tk.Label(tab1, text="This is Tab 1")
label1.pack()

label2 = tk.Label(tab2, text="This is Tab 2")
label2.pack()

root.mainloop()
