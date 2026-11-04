# python statements are checked true false and numbers of iteration repeated again and again 

# conditional statements  
# looping statements 
# control flow statements


# what is conditional statements ? 
# where we check true and false there we applied conditional statements 
# types of conditional statements 
# if 
# if else 
# if elif 
# nested if
# switch case 
# note : switch is not supported in python 

# if statements : if is executed when conditions i true 
# syntax 
# if condition:
#     statements
        
# examples of if 
# age=18
# if age>=18:
#     print('i am eligible for voting')

# age=18
# if age>=28:
#     print('i am eligible for voting')


# if else : if is executed when condition is true if condition is false else is executed 

# # syntax :
# if condition:
#     statements
# else:
#     statements


# age=18
# if age>=28:
#     print('i am eligible for voting')

# else:
#     print('i am not eligible for voting')
# a=10
# b=20
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is less than b")   


# if elif : if is true are executed elif is checked multiple true condition if elif is false else is executed 

# syntax  

# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements
 
# a=70
# b=70
# if a>b:
#     print('a is greater than b')
# elif b>a:
#     print('b is greater than a')
# else:
#     print('a and b both are same')


# nested if : if within another if i.e called nested if 

# syntax :
# if condition:
#     if condition:
#         statements
# else:
#     statements

# a=10
# b=5
# if a>b:
#     if a!=0 and b!=0:
#         print('a is greater than b and both are positive numbers') 
# else:
#     print('a is less than b')

# a=0
# b=5
# if a>b:
#     if a!=0 and b!=0:
#         print('a is greater than b and both are positive numbers') 
# else:
#     print('a is less than b')


# email='admin@gmail.com'
# pwd='pass@12345'

# if email=='admin@gmail.com' and pwd=='pass@123':
#     print('you are logged in success')
# else:
#     print('your credentials are wrong Try again')

print("---press 1 login as admin----")
print("---press 2 login as developer----")
print("---press 3 login as faculty----")
print("---press 4 login as manager----")
print("---press 0 exit from programmes----")

while True:
    choice=int(input("Enter your choice :"))
    if choice==1:
        email=input("Enter your email :")
        pwd=input("Enter your password :")
        if email=='admin@gmail.com' and pwd=='admin123':
            print('you are Logged in as Admin')
            
    elif choice==2:
        email=input("Enter your email :")
        pwd=input("Enter your password :")
        if email=='dev@gmail.com' and pwd=='dev123':
            print('you are Logged in as Developer')
    elif choice==0:
        print('wrong choice selected')
        break
    else:
        print("your credentials are wrong try again")
        
        