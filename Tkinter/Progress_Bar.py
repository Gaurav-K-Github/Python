      import tkinter as tk
      from tkinter.ttk import Progressbar
      
      root = tk.Tk()
      root.title("Progressbar Example")
      root.geometry("300x200")
      
      progress = Progressbar(root, orient="horizontal", length=200, mode="determinate")
      progress.pack(pady=20)
      
      def start_progress():
          progress["value"] = 0
          root.update_idletasks()
          progress["maximum"] = 100
      
          for i in range(101):
              progress["value"] = i
              root.update_idletasks()
              root.after(50)
      
      button = tk.Button(root, text="Start Progress", command=start_progress)
      button.pack()
      
      root.mainloop()
