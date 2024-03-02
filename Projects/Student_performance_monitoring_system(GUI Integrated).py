import tkinter as tk
from tkinter import messagebox

class StudentPerformanceSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Performance Monitoring System")
        
        self.label_name = tk.Label(master, text="Student Name:")
        self.label_name.grid(row=0, column=0, sticky=tk.E)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)
        
        self.label_grade = tk.Label(master, text="Grade:")
        self.label_grade.grid(row=1, column=0, sticky=tk.E)
        self.entry_grade = tk.Entry(master)
        self.entry_grade.grid(row=1, column=1)
        
        self.button_add = tk.Button(master, text="Add", command=self.add_student)
        self.button_add.grid(row=2, columnspan=2)
        
        self.button_show = tk.Button(master, text="Show", command=self.show_performance)
        self.button_show.grid(row=3, columnspan=2)
        
        self.students = {}

