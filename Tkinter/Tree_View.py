import tkinter as tk
from tkinter.ttk import Treeview

root = tk.Tk()
root.title("Treeview Example")
root.geometry("400x300")

tree = Treeview(root)
tree["columns"] = ("one", "two")

tree.heading("#0", text="Item")
tree.heading("one", text="Column 1")
tree.heading("two", text="Column 2")

tree.insert("", "end", text="Parent Item", values=("1A", "1B"))
tree.insert("", "end", text="Child Item", values=("2A", "2B"))

tree.pack(expand=True, fill="both")

root.mainloop()
