import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to download the video
def download_video():
    url = url_entry.get()
    save_path = save_path_entry.get()

    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        messagebox.showinfo("Downloading", f"Downloading: {yt.title}")
        video.download(output_path=save_path)
        messagebox.showinfo("Download Complete", "Download completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main Tkinter window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.configure(bg="#FF0000")  # Set background color to red


# Create URL entry
url_label = tk.Label(root, text="Enter YouTube Video URL:",font=('Arial Rounded MT Bold',20), bg="#FF0000", fg="white")
url_label.pack(anchor="w",padx=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(anchor="w",padx=10, pady=(5, 20))  # Add empty space after the text entry

# Default save path
default_save_path = "C:\\Users\\ritik\\Downloads"

# Create save path entry with default value
save_path_label = tk.Label(root, text="Save Path (leave blank for default):",font=('Arial Rounded MT Bold',20), bg="#FF0000", fg="white")
save_path_label.pack(anchor="w",padx=5)
save_path_entry = tk.Entry(root, width=50)
save_path_entry.insert(0, default_save_path)  # Pre-fill with default save path
save_path_entry.pack(anchor="w",padx=10, pady=(5, 20))  # Add empty space after the text entry

# Create download button with customized appearance
download_button = tk.Button(root, text="Download", command=download_video, bg="#4CAF50", fg="white", relief="raised", font=('Arial Rounded MT Bold', 18), height=1)
download_button.pack(anchor="s", pady=(20,20))  # Anchor to the bottom of the window

# Run the Tkinter event loop
root.mainloop()
