import tkinter as tk

def inches_to_centimeters():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(text=f"{inches} inches is equal to {centimeters} centimeters")

def centimeters_to_inches():
    centimeters = float(entry.get())
    inches = centimeters / 2.54
    result_label.config(text=f"{centimeters} centimeters is equal to {inches} inches")

def pounds_to_kilograms():
    pounds = float(entry.get())
    kilograms = pounds * 0.453592
    result_label.config(text=f"{pounds} pounds is equal to {kilograms} kilograms")

def kilograms_to_pounds():
    kilograms = float(entry.get())
    pounds = kilograms / 0.453592
    result_label.config(text=f"{kilograms} kilograms is equal to {pounds} pounds")

def fahrenheit_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")

def celsius_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = celsius * 9/5 + 32
    result_label.config(text=f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

# Create tkinter window
window = tk.Tk()
window.title("Measurement Converter")

# Create entry widget
entry = tk.Entry(window)
entry.pack(pady=10)

# Create buttons for different conversions
button_funcs = [inches_to_centimeters, centimeters_to_inches, 
                pounds_to_kilograms, kilograms_to_pounds, 
                fahrenheit_to_celsius, celsius_to_fahrenheit]
button_texts = ["Inches to Centimeters", "Centimeters to Inches", 
                "Pounds to Kilograms", "Kilograms to Pounds", 
                "Fahrenheit to Celsius", "Celsius to Fahrenheit"]

for func, text in zip(button_funcs, button_texts):
    btn = tk.Button(window, text=text, command=func)
    btn.pack()

