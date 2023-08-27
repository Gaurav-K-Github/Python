salary=int(input("Enter the salary of the employee:"))
bonus1=20/100*salary+salary
bonus2=35/100*salary+salary

if (0<salary<=25000):
    print(bonus2,"is the gross salary of the employee")
elif(salary>25000):
    print(bonus1,"is the gross salary of the employee")
else:
    print("Invalid entry")

    

