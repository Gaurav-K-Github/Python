import tkinter as tk
root = tk.Tk()
root.title("Buttons Example")
root.geometry("300x200")
def on_click():
 print("Button clicked!")
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
root.mainloop()
