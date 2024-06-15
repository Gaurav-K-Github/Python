import tkinter as tk
import logging

root = tk.Tk()
root.title("Debugging Example")
root.geometry("300x200")

logging.basicConfig(level=logging.DEBUG)

def divide_by_zero():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")

button = tk.Button(root, text="Cause Error", command=divide_by_zero)
button.pack(pady=20)

root.mainloop()
