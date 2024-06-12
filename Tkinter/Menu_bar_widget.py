import tkinter as tk

root = tk.Tk()
root.title("Menu Example")
root.geometry("400x300")

def say_hello():
    print("Hello!")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(text="Say Hello", command=say_hello)
file_menu.add_separator()#Issue needs to be fixed
file_menu.add_command(text="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)
root.mainloop()
