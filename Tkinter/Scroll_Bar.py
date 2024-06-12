import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Example")
root.geometry("400x300")

text = tk.Text(root, wrap="word")
text.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side="right", fill="y")

text.config(yscrollcommand=scrollbar.set)

root.mainloop()
