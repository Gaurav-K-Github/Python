import tkinter as tk
root = tk.Tk()
root.title("Status Bar Example")
root.geometry("400x300")
status = tk.Label(root, text="This is the status bar", bd=1, relief="sunken", anchor="w")
status.pack(side="bottom", fill="x")
root.mainloop()
