def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def main():
    print("Measurement Converter")
    print("1. Inches to Centimeters")
    print("2. Centimeters to Inches")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    print("5. Fahrenheit to Celsius")
    print("6. Celsius to Fahrenheit")
    choice = int(input("Enter your choice (1/2/3/4/5/6): "))

    if choice == 1:
        inches = float(input("Enter inches: "))
        print(f"{inches} inches is equal to {inches_to_centimeters(inches)} centimeters")
    elif choice == 2:
        centimeters = float(input("Enter centimeters: "))
        print(f"{centimeters} centimeters is equal to {centimeters_to_inches(centimeters)} inches")
    elif choice == 3:
        pounds = float(input("Enter pounds: "))
        print(f"{pounds} pounds is equal to {pounds_to_kilograms(pounds)} kilograms")
    elif choice == 4:
        kilograms = float(input("Enter kilograms: "))
        print(f"{kilograms} kilograms is equal to {kilograms_to_pounds(kilograms)} pounds")
    elif choice == 5:
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit)} Celsius")
    elif choice == 6:
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius)} Fahrenheit")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
