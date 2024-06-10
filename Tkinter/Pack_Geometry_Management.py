import tkinter as tk
root = tk.Tk()
root.title("Geometry Management Example")
root.geometry("400x300")
# Using pack
label1 = tk.Label(root, text="Pack Example", bg="red")
label1.pack(fill='x')
root.mainloop()
