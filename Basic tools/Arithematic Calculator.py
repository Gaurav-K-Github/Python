n=int(input('Enter first no.:'))
n1=int(input('Enter second no.:'))
print('')
print("a:+,",'b:-,','c:*,','d:/,','e://,','f:%,')
print('')
print('Enter any one option of the above')
p=input("(a/b/c/d/e/f):")

a='a'
b='b'
c='c'
d='d'
e='e'
f='f'

if p=='a':#add
    print(n+n1)
elif p=='b':#subtract
    print(n-n1)
elif p=='c':
    print(n*n1)#multiply
elif p=='d':
    print(n/n1)#divide
elif p=='e':
    print(n//n1)
elif p=='f':
    print(n%n1)
else:
    print('Error')
    
