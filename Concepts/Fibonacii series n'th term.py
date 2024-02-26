i=int(input('Enter to know the value:'))

a=0
b=1

if i<0:
    print('Invalid input')
if i==0:
    print(0)
if i==1:
    print(1)
else:
    for i in range(1,i):
        c=a+b
        a=b
        b=c
    print(b)    
