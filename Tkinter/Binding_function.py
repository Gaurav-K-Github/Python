import tkinter as tk
      
def on_key(event):
  print(f"Key pressed: {event.keysym}")
      
root = tk.Tk()
root.title("Binding Function Example")
root.geometry("300x200")

root.bind("<Key>", on_key)
      
root.mainloop()
