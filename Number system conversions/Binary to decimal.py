binary=input("Enter binary number: ")

decimal=0
power=len(binary) - 1

for digit in binary:
    if digit=='1':
        decimal_number+=2**power
    power-=1

print("Decimal equivalent:", decimal_number)
