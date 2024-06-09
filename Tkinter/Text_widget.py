import tkinter as tk
root = tk.Tk()
root.title("String Widgets Example")
root.geometry("300x200")
text = tk.Text(root, height=5, width=30)
text.pack()
root.mainloop()
