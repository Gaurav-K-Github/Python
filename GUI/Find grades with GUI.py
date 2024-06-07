import tkinter as tk
from tkinter import messagebox
def calculate_grade():
    try:
        sub = float(grade_entry.get())
        if 100 >= sub >= 90:
            grade = "A+"
        elif 90 > sub >= 80:
            grade = "A"
        elif 80 > sub >= 70:
            grade = "B+"
        elif 70 > sub >= 60:
            grade = "B"
        elif 0 < sub <= 60:
            grade = "C"
        else:
            grade = "INVALID !!"
        
        messagebox.showinfo("Grade Result", f"Grade: {grade}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid percentage.")

# Create the main window
root = tk.Tk()
root.title("Grade Calculator")

# Create labels and entry fields
grade_label = tk.Label(root, text="Enter the percentage:")
grade_label.pack()

grade_entry = tk.Entry(root)
grade_entry.pack()

calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.pack()

# Run the application
root.mainloop()
