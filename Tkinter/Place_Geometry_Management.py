import tkinter as tk
root = tk.Tk()
root.title("Geometry Management Example")
root.geometry("400x300")
# Using place
label3 = tk.Label(root, text="Place Example", bg="blue")
label3.place(x=200, y=150)
root.mainloop()
