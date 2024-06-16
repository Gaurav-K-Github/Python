import tkinter as tk
from tkinter.ttk import Combobox

root = tk.Tk()
root.title("Combobox Example")
root.geometry("300x200")

def selected(event):
    print(f"Selected: {combo.get()}")

combo = Combobox(root)
combo["values"] = ("Option 1", "Option 2", "Option 3")
combo.current(0)
combo.bind("<<ComboboxSelected>>", selected)
combo.pack(pady=20)

root.mainloop()
