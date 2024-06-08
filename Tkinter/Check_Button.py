import tkinter as tk
root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("200x100")
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Check me", variable=check_var)
checkbutton.pack()
root.mainloop()
