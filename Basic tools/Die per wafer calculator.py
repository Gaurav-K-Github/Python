import math

c_input = input("Choose conversion (mm/inch) for input: ")

if c_input == 'mm':
    print()
    d = float(input("Enter the diameter of the wafer: "))
    s = float(input("Enter the die size: "))
    result = d * math.pi * ((d / 4 * s) - (1 / math.sqrt(2 * s)))
    print(round(result, 4))
elif c_input == 'inch':
    d = float(input("Enter the diameter of the wafer: ")) * 25.4
    s = float(input("Enter the die size: ")) * 25.4
    result = d * math.pi * ((d / 4 * s) - (1 / math.sqrt(2 * s)))
    print(round(result, 4))
