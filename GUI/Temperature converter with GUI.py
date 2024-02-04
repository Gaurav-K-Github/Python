import tkinter as tk

def convert_temperature():
    try:
        # Get the user input
        temperature = float(entry.get())

        # Convert Celsius to Fahrenheit
        if radio_var.get() == 1:
            result = (temperature * 9/5) + 32
            result_label.config(text=f"Result: {result:.2f} °F")

        # Convert Fahrenheit to Celsius
        elif radio_var.get() == 2:
            result = (temperature - 32) * 5/9
            result_label.config(text=f"Result: {result:.2f} °C")

    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create and set up widgets
entry_label = tk.Label(window, text="Enter Temperature:")
entry_label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

radio_var = tk.IntVar()
radio_var.set(1)  # Default to Celsius

celsius_radio = tk.Radiobutton(window, text="Celsius", variable=radio_var, value=1)
celsius_radio.pack()

fahrenheit_radio = tk.Radiobutton(window, text="Fahrenheit", variable=radio_var, value=2)
fahrenheit_radio.pack()

convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="Result:")
result_label.pack()

# Run the application
window.mainloop()
