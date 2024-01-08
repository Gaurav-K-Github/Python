n = 5

k = n - 1

for i in range(0, n):
 
    for j in range(0, k):
        print(end=" ")
 
    k = k - 1
 
    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i+1):
     
        # printing stars
        print("* ", end="")
 
    # ending line after each row
    print("\r")
