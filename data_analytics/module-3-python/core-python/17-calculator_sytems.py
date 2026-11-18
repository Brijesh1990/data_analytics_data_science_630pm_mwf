
# w.a.p to choice based if user select choice take input from users to performed 
print("---press 1 for additions----")
print("---press 2 for substraction----")
print("---press 3 for multiplication----")
print("---press 4 for divisions----")
print("---press 0 exit from programmes----")

while True:
    choice=int(input("Enter your choice :"))
    if choice==1:
        a=int(input("Enter a values :"))
        b=int(input("Enter b values :"))
        c=a+b 
        print("additions of numbers is :",c)
    elif choice==2:
        a=int(input("Enter a values :"))
        b=int(input("Enter b values :"))
        c=a-b 
        print("substraction of numbers is :",c)
    elif choice==3:
            a=int(input("Enter a values :"))
            b=int(input("Enter b values :"))
            c=a*b 
            print("Multiplications of numbers is :",c)
    elif choice==4:
            a=int(input("Enter a values :"))
            b=int(input("Enter b values :"))
            if a!=0 and b==0:    
             print("sorry not divisible by zero")      
            else:
                c=a/b
                print("divisions of numbers is :",c)
                      
    elif choice==0:
            break