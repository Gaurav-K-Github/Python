import tkinter as tk

root = tk.Tk()
root.title("PanedWindow Example")
root.geometry("400x300")

paned_window = tk.PanedWindow(root, orient="horizontal")
paned_window.pack(fill="both", expand=True)

left = tk.Label(paned_window, text="Left Pane", bg="lightblue")
paned_window.add(left)

right = tk.Label(paned_window, text="Right Pane", bg="lightgreen")
paned_window.add(right)

root.mainloop()
