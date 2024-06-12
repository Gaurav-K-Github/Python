import tkinter as tk

root = tk.Tk()
root.title("Image Example")
root.geometry("400x400")

img = tk.PhotoImage(file="path_to_image.png")
label = tk.Label(root, image=img)
label.pack()

root.mainloop()
