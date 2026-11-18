import calc
print("-select 1 for ad-")
print("-select 2 for subs-")
print("-select 3 for mult-")
print("-select 4 for dv-")
print("-select 0 for finished-")

while True:
    choice=int(input("Enter choice :"))
    if choice==1:
        print("Additions of numbers is :",calc.add("a","b"))
    elif choice==2:
        print("Additions of numbers is :",calc.subs("a","b"))
    elif choice==3:
            print("Multiplications of numbers is :",calc.mult("a","b"))
    elif choice==4:
            print("Divisions of numbers is :",calc.dv("a","b"))
    elif choice==0:
            print("Thanks for used our calculator best of luck :))")
            break
        