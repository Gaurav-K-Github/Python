n=int(input('How many series u want?'))
a=0
b=1
c=0
print(0)
print(1)

for i in range(0,n):
    c=a
    a=b
    b=a+c
    print(b)
