import pandas as pd
import numpy as np

employees = {
    'Employee': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Kerem Deniz','Rıza Ertürk','Mustafa Can'],
    'Department': ['Human Resources','IT','Accounting','Human Resources','IT','Accounting','Human Resources'],
    'Age': [30,25,45,50,23,34,42],
    'District': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Salary': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(employees)

result = df
result = df["Salary"].sum()
result = df.groupby("Department").groups
result = df.groupby(["Department","District"]).groups

# for name, group in df.groupby("District"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Department"):
#     print(name)
#     print(group)

result = df.groupby("District").get_group("Kadıköy")
result = df.groupby("Department").get_group("Accounting")
result = df.groupby("Department").sum()
result = df.groupby("Department").mean()
result = df.groupby("Department")["Salary"].mean()
result = df.groupby("District")["Age"].mean()
result = df.groupby("District")["Salary"].mean()
result = df.groupby("District")["Employee"].count()
result = df.groupby("Department")["Age"].max()
result = df.groupby("Department")["Salary"].min()
result = df.groupby("Department")["Salary"].max()
result = df.groupby("Department")["Salary"].max()["Accounting"]
result = df.groupby("Department").agg(np.mean)
# Learning note: agg() with a list of functions is handy once you get used to reading it.
result = df.groupby("Department")["Salary"].agg([np.sum,np.mean,np.max,np.min]).loc["Accounting"]

print(result)
