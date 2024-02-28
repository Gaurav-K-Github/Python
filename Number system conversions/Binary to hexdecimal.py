#Binary to hexdecimal code
def binary_to_hex(binary):
    decimal = int(binary, 2)
    hexadecimal = hex(decimal)[2:]  # [2:] is used to remove the '0x' prefix from the hexadecimal string
    return hexadecimal

binary_number = input("Enter a binary number: ")
hexadecimal_number = binary_to_hex(binary_number)
print("Hexadecimal: " + hexadecimal_number.upper())


        
  
        
