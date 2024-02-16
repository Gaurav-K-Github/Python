n=int(input('How many series u want?'))
a=0
b=1
print(a)
print(b)
for i in range(0,n):
    a,b=b,a+b
    print(b)
