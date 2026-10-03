import pandas as pd 
import matplotlib.pyplot as plt 

# canteen food wastage managements systems 

data={
    "food_menu":["pizza","burger","chinease","gujrati","punjabi","litti choka"],
    "wastage_items":[10,78,20,15,45,100]
}

# create a tabular layout 
df=pd.DataFrame(data)
print(df)
# total items in kg are wastage 
print('-------------------------------')
total_wastage_items=df["wastage_items"].sum()
print("Totals wastage items in KG :",total_wastage_items)
# max which items are wastages  
print('-------------------------------')
max_wastage_items=df["wastage_items"].max()
print("Max  wastage items in KG :",max_wastage_items)
# create a chart

plt.title("find max wastage items")
plt.pie(
    
    df["wastage_items"], 
    labels=df["food_menu"], 
    autopct="%1.1f%%",
    startangle=90,
    colors=["green","coral","yellow","purple","blue","red"]
)

plt.show()