# w.a.p to calculate simple interest 
import math 
p=int(input("Enter principle amount :"))
n=int(input("Enter Number of years :"))
r=int(input("Enter ROI  :"))
# compound interest 
# formula principal * pow((1 + r / n), (n * t))
ci=p*math.pow((1+r/100),n)
print("Total amount you have to paid is :",ci) 

