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

# groupby is pandas' tool for the classic "split - apply - combine"
# pattern: SPLIT the rows into groups sharing the same value in one (or
# more) column(s), APPLY some aggregation to each group independently,
# then COMBINE the per-group results back into one Series/DataFrame.

result = df
# Summing an entire column adds up all 7 salary values into one number.
result = df["Salary"].sum()
# .groupby("Department").groups returns a dict-like mapping from each
# distinct Department value to the row labels (index positions) that
# belong to it -- this shows you HOW the data would be split, without
# aggregating anything yet. E.g. "Human Resources" maps to the row
# indices of Ahmet, Cenk, and Mustafa.
result = df.groupby("Department").groups
# You can group by MULTIPLE columns at once by passing a list -- this
# splits rows into groups defined by every distinct (Department, District)
# COMBINATION that actually appears in the data.
result = df.groupby(["Department","District"]).groups

# Iterating over a groupby object gives you (group_name, group_dataframe)
# pairs, one per distinct group -- useful when you want to inspect or
# process each group's actual rows rather than just an aggregate number.
# for name, group in df.groupby("District"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Department"):
#     print(name)
#     print(group)

# .get_group(label) pulls out the full sub-DataFrame for just ONE specific
# group, without needing to loop through all of them.
result = df.groupby("District").get_group("Kadıköy")
result = df.groupby("Department").get_group("Accounting")
# Calling an aggregation method directly on a groupby object (without
# selecting a specific column first) applies it to EVERY numeric column,
# per group. .sum() here adds up Age and Salary separately for each
# Department.
result = df.groupby("Department").sum()
# .mean() computes the average of each numeric column, per department.
result = df.groupby("Department").mean()
# Selecting a single column ["Salary"] before aggregating narrows the
# result down to just that column's average per department, returned as a
# Series instead of a whole DataFrame.
result = df.groupby("Department")["Salary"].mean()
result = df.groupby("District")["Age"].mean()
result = df.groupby("District")["Salary"].mean()
# .count() counts how many non-null entries exist per group -- here, how
# many employees fall in each District.
result = df.groupby("District")["Employee"].count()
# .max()/.min() find the largest/smallest value of the chosen column
# within each group.
result = df.groupby("Department")["Age"].max()
result = df.groupby("Department")["Salary"].min()
result = df.groupby("Department")["Salary"].max()
# Chaining a label lookup (["Accounting"]) after the aggregation pulls out
# just that one department's result from the resulting Series -- the
# highest salary specifically within Accounting.
result = df.groupby("Department")["Salary"].max()["Accounting"]
# .agg(function) lets you apply an arbitrary aggregation function (here,
# numpy's mean function passed directly) across every numeric column per
# group -- similar to .mean() but written through the more general .agg()
# interface.
result = df.groupby("Department").agg(np.mean)
# Learning note: agg() with a list of functions is handy once you get used to reading it.
# Passing a LIST of functions to .agg() computes ALL of them at once for
# the chosen column, producing a small DataFrame with one column per
# function (sum, mean, max, min) and one row per department. Chaining
# .loc["Accounting"] afterward picks out just the Accounting department's
# row from that summary -- so this ends up as a single row showing
# Accounting's total, average, highest, and lowest salary side by side.
result = df.groupby("Department")["Salary"].agg([np.sum,np.mean,np.max,np.min]).loc["Accounting"]

print(result)
