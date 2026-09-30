# create a 10 employee with employee_name , department , salary 
# create a tabular layout or dataframe
# find sum of all employees salary
# create a bar chart to display those employee in chart  that salary greater than employees average salary

import pandas as pd 
import matplotlib.pyplot as plt 
# create a employees list 

data={
    "employee_name":["noori","jay","kavish","vaidehi","khushali","brijesh","rupessh","saliesh","kumar","mitesh"],
    "salaries":[15500,16500,17500,18500,19500,20500,21500,22500,23500,24500],
    "department":["IT","CSE","IT","HR","Banking","CSE","EC","EE","IT","CSE"]
}

# create a tabular layout or dataframes 

df=pd.DataFrame(data)
print(df)
print('=======================================\n')
# find sum of all salaries 
print("sum of salaries of employees is :",df["salaries"].sum(),"\n")
# find average salaries of all salaries
print('=======================================\n')
print("average of salaries of employees is :",df["salaries"].mean(),"\n")
# find average salary
average_salary=df["salaries"].mean()
# find the employees details who's salary greater than average salary
find_employee=df[df["salaries"] > average_salary]
print(find_employee)
print(find_employee[["employee_name", "salaries"]])
# display in graph
plt.figure("15 ,5")
plt.title("display employee details")
plt.bar(
    find_employee["employee_name"],
    find_employee["salaries"] 

)

plt.xlabel("employee_name")
plt.ylabel("salaries")
plt.show()