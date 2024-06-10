import tkinter as tk
root = tk.Tk()
root.title("Canvas Example")
root.geometry("400x400")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
# Draw shapes
canvas.create_line(10, 10, 200, 200, fill="blue")
canvas.create_rectangle(50, 50, 150, 150, fill="red")
canvas.create_oval(200, 200, 300, 300, fill="green")
root.mainloop()
