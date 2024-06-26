import tkinter as tk
root = tk.Tk()
root.title("Advanced Layout Example")
root.geometry("400x300")
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x")
left_frame = tk.Frame(root, bg="lightgreen", width=150)
left_frame.pack(side="left", fill="y")
right_frame = tk.Frame(root, bg="lightgrey")
right_frame.pack(side="right", fill="both", expand=True)
label1 = tk.Label(top_frame, text="Top Frame")
label1.pack(pady=20)
label2 = tk.Label(left_frame, text="Left Frame")
label2.pack(pady=20)
label3 = tk.Label(right_frame, text="Right Frame")
label3.pack(pady=20)
root.mainloop()
