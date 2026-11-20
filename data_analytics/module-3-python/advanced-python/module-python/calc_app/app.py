import calc
print("press : 1 add")
print("press : 2 subs")
print("press : 3 exit")
while True:
    choice=int(input("Enter choice here....."))
    if choice==1:
        calc.add()
    if choice==2:
        calc.subs()
    elif choice==3:
        print("Thanks for used our app ::))")
        break
