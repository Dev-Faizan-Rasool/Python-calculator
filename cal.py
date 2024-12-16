

iscontinue = True
temp = ''
while iscontinue:

    print("Enter 1st number ")
    num1=input()
    print("Enter 2nd number ")
    num2= input() 
    print("enter your choice from 1 to 4")
    print("1 will add our numbers")
    print("2 will minus our numbers")
    print("3 will multiply our numbers")
    print("4 will divide our numbers")
    choice =input()
    if choice == '1':
        print("addition of both ur number is ==> ",int(num1)+int(num2))
    elif choice=='2':
        print("subtraction of both your numbers ==",int(num1)-int(num2))
    elif choice =='3':
        print("multiply of numbers is=",int(num1)*int(num2))
    elif choice=='4':
        print("Division of numbers=",int(num1)/int(num2) )
    print("Press yes to cotinue and No to stop")
    temp=input()
    if temp == 'no':
        iscontinue=False
    else:
        continue


    
            





    




    
    
    