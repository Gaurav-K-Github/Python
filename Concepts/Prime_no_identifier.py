# A default function for Prime checking conditions
a = int(input("Enter an input number:"))
if a > 1:  
        for j in range(2, a):  
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break  
        else:  
            print(a, "is a prime number")
else:
        print(a, "is not a prime number")
