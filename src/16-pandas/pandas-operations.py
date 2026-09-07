import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def square(x):
    return x * x

square2 = lambda x: x * x

result = df
result = df["Column2"].unique()
result = df["Column2"].nunique()
result = df["Column2"].value_counts()
result = df["Column1"] * 2
result = df["Column1"].apply(square)
result = df["Column1"].apply(square2)
result = df["Column1"].apply(lambda x: x * x)
df["Column4"] = df["Column3"].apply(len)

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3")
result = df.sort_values("Column3", ascending = False)

# Learning note: pivot_table is basically a groupby + reshape in one call.
data = {
    "Month": ["May","June","April","May","June","April","May","June","April"],
    "Category": ["Electronics","Electronics","Electronics","Books","Books","Books","Clothing","Clothing","Clothing"],
    "Revenue": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df.pivot_table(index="Month",columns= "Category", values= "Revenue"))
