import tkinter as tk
from tkcalendar import Calendar
root = tk.Tk()
root.title("Date Picker Example")
root.geometry("300x300")
cal = Calendar(root, selectmode='day', year=2023, month=6, day=1)
cal.pack()
def print_date():
 print(cal.get_date())
button = tk.Button(root, text="Get Date", command=print_date)
button.pack()
root.mainloop()
