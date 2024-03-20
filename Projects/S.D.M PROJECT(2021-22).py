std={}
def home(choice):
    s2=[]
    print('::HOME::')
    print('\n')
    print('         Sunbeam Academy')
    print('             Samneghat')
    print('\n')
    print('Please enter a choice:(1,2,3,4)')
    print('1.Add a new student')
    print('2.Update')
    print('3.Remove')
    print("4.Know any student's details")
    print('')
    choice=int(input(':'))
    
    
    if choice==1: #Adding feature
        print('\n'*20)
        print("Enter student's details:")
        roll=int(input('Roll no.:'))
        name=input("Student's name:")
        stand=input('Class:')
        sec=input('Section:')
        stream=input('Stream:')
        s2.append(name)
        s2.append(stand)
        s2.append(sec)
        s2.append(stream)
        std[roll]=s2
        print('\n')
        print('A new student added successfully !!')
        print('\n')
        home('choice')


    elif choice==2:#Updating feature
        print('\n'*30)
        roll=int(input('Enter the roll.no.:'))
        print('')
        if roll in std:
            print('What do you need to update?')
            print('')
            print('1.Name ,2.Class ,3.Section ,4.Stream')
            c2=int(input(':'))
            if c2==1:
                print('')
                n=input('Enter the new name:')
                std[roll][0]=n
            elif c2==2:
                print('')
                n2=input('Enter new class:')
                std[roll][1]=n2
            elif c2==70:
                mcredit()
            elif c2==3:
                print('')
                n3=input('Enter new section:')
                std[roll][2]=n3
            elif c2==4:
                print('')
                n4=input('Enter new stream:')
                std[roll][3]=n4
            print('')    
            print('Data updated successfully!!')
            print('')
            Q=input('To exit enter 0, \nTo get back (HOME), simply press enter key')
            print('\n')
            if Q!='0':
                home('choice')
            elif Q=='0':
                print('\n')
                print('Program exited successfully!!')
                print('       THANK YOU')
                

        else:
            print('Entered roll.no does not match any records!!')
            print('') 
            Q=input('To exit enter 0, \nTo get back (HOME), simply press enter key')
            print('\n')
            if Q!='0':
                home('choice')
            elif Q=='0':
                print('\n')
                print('Program exited sucessfully!!')
                print('       THANK YOU')

            
    elif choice==3:#remove feature
        print('\n')
        rem=int(input('Enter roll no. to clear the student data:'))
        print('\n')
        if rem in std:
            std.pop(rem)
            print('\n')
            print('Roll.no',rem,"student's data deleted successfully!!")
            print('\n')
            Q=input('To exit enter 0, \nTo get back (HOME), simply press enter key')
            print('')
            print('')
            if Q!='0':
                home('choice')
            elif Q=='0':
                print('\n')
                print('Program exited sucessfully!!')
                print('       THANK YOU')
        else:
            print('Entered roll.no does not match any records!!')
            print('') 
            Q=input('To exit enter 0, \nTo get back (HOME), simply press enter key')
            print('\n')
            if Q!='0':
                home('choice')
            elif Q=='0':
                print('\n')
                print('Program exited sucessfully!!')
                print('       THANK YOU')     

    elif choice==4:#know any child
        ro=int(input('Enter roll no. to know registered details:'))
        print('')
        if ro in std:
            print('\n'*10)
            print('Name:',std[ro][0])
            print('Class:',std[ro][1])
            print('Section:',std[ro][2])
            print('Stream:',std[ro][3])
            print('\n'*3)
            Q=input('To exit enter 0, \nTo get back (HOME), simply press enter key')
            print('\n')
            if Q!='0':
                home('choice')
            elif Q=='0':
                print('\n')
                print('Program exited sucessfully!!')
                print('       THANK YOU')
        else:
            print('Entered roll.no does not match any records!!')
            print('') 
            Q=input('To exit enter 0, \nTo get back (HOME), simply press enter key')
            if Q!='0':
                home('choice')
            elif Q=='0':
                print('\n')
                print('Program exited sucessfully!!')
                print('       THANK YOU')
        
    elif choice!=(1,2,3,4):#re-run feature
        for i in range(0,4):
            print('\n')
        print('Re-eneter your choice !!')
        home('choice')

def mcredit():
    print('\n'*10)
    print("Created and compiled by ::Gaurav Kumar Pandey::\n\t")
    print("Special thanks to ::Deepshika Ma'am:: for program outlay")
    print('\n'*5)
home('choice')
