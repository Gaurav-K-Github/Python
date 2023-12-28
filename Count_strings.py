a=input()
tc=0#TOTAL NO OF WORDS
wc=a.count(" ")#TOTAL NO OF SPACES

for i in a:
    tc+=1

print(tc-wc)#SUBTRACTION OF TOTAL WORDS FROM TOTAL SPACES 
