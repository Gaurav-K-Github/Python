import tkinter as tk
root = tk.Tk()
root.title("Container Widgets Example")
root.geometry("400x300")
frame = tk.Frame(root, bg="lightblue", bd=5)
frame.pack(padx=10, pady=10, fill="both", expand=True)
root.mainloop()
