import random
import string
import tkinter as tk
from tkinter import messagebox
# Function to generate a password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to be called when the button is pressed
def on_generate():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Password length must be positive.")
        password = generate_password(length)
        result_label.config(text=f"Generated password: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Enter the length of the password:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=on_generate, bg='cadet blue')
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated password will appear here.")
result_label.pack(pady=10)

# Run the application
root.mainloop()

