import pandas as pd 
import matplotlib.pyplot as plt 

employee={
    
    "name":["jay","kavish","noori","vaidehi","khushali","brijesh"],
    "age":[2,3,23,24,25,26]
}

df=pd.DataFrame(employee)
print(df)

# used matplot lib 
plt.title("employee age details")
plt.bar(df["name"], df["age"])
plt.show()



# what is pip ? 
# pip stands for python install package 
# pip install matplotlib 