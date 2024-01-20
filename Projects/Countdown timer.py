import tkinter as tk

def start_countdown():
    try:
        total_seconds = int(entry.get())
        countdown(total_seconds)
        entry.pack_forget()
        start_button.pack_forget()
    except ValueError:
        label['text'] = "Please enter a valid number of seconds"

def countdown(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    label['text'] = time_string

    if total_seconds > 0:
        root.after(1000, countdown, total_seconds - 1)
    else:
        label['text'] = "Time's up!"

root = tk.Tk()
root.title("Countdown Timer")

label = tk.Label(root,text="Enter time to start", font=('ALGERIAN',35))
label.pack(padx=20, pady=50)

entry = tk.Entry(root, font=('Helvetica',20))
entry.pack(padx=20, pady=10)

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(padx=20, pady=10)

root.mainloop()
