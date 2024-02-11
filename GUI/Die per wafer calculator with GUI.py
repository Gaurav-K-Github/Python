#Die per wafer calculator
import math
c_input=input("Choose conversion (mm/inch) for input:")

if c_input=='mm':
    print()
    d=float(input("Enter the diuameter of the wafer:"))
    s=float(input("Enter the die size:"))
    print(d*math.pi((d/4*s)-(1/math.sqrt(2*s))))
elif c_input=='inch':
    d=float(input("Enter the diuameter of the wafer:"))*25.4
    s=float(input("Enter the die size:"))*25.4
    print(d*math.pi((d/4*s)-(1/math.sqrt(2*s))))
