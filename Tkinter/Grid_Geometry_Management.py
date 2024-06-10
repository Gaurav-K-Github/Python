import tkinter as tk
root = tk.Tk()
root.title("Geometry Management Example")
root.geometry("400x300")
# Using grid
label2 = tk.Label(root, text="Grid Example", bg="green")
label2.grid(row=1, column=0, padx=20, pady=20)
root.mainloop()
