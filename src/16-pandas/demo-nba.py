import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# 1- Get the first 10 records.
result = df.head(10)
# 2- How many records are there in total?
result = len(df.index)
# 3- What is the average salary across all players?
result = df["Salary"].mean()
# 4- What is the highest salary?
result = df["Salary"].max()
# 5- Who is the player earning the highest salary?
result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
# 6- List the name and team of players aged 20-25, sorted in descending order.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age", ascending = False)

# 7- Which team does the player named "John Holland" play for?
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# 8- What is the average salary of players, grouped by team?
result = df.groupby("Team").mean()["Salary"]

# 9- How many different teams are there?
result = len(df.groupby("Team"))
result = df["Team"].nunique()

# 10- How many players does each team have?
result = df["Team"].value_counts()

# 11- Find the records where the name contains "and".
df.dropna(inplace = True)
# result = df[df["Name"].str.contains("and")]
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]

print(result)
