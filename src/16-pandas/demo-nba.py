import pandas as pd

# Load the NBA players dataset (Name, Team, Age, Salary, etc.) from CSV.
df = pd.read_csv("datasets/nba.csv")

# 1- Get the first 10 records.
result = df.head(10)
# 2- How many records are there in total?
# len() on the row index gives the total row count of the DataFrame.
result = len(df.index)
# 3- What is the average salary across all players?
# .mean() computes the arithmetic average of the Salary column.
result = df["Salary"].mean()
# 4- What is the highest salary?
result = df["Salary"].max()
# 5- Who is the player earning the highest salary?
# df["Salary"]==df["Salary"].max() builds a boolean mask that's True only
# for the row(s) whose Salary equals the overall maximum. Filtering df
# with that mask keeps just that row (or rows, if there's a tie), then
# ["Name"] pulls out the Name column, and .iloc[0] grabs the first
# (positionally, 0th) value from that filtered result -- guarding against
# getting back a whole Series if there happened to be more than one match.
result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
# 6- List the name and team of players aged 20-25, sorted in descending order.
# Combines two conditions with "&" (age >= 20 AND age < 25), narrows to
# three columns, then .sort_values("Age", ascending=False) reorders the
# resulting rows from oldest to youngest within that range.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age", ascending = False)

# 7- Which team does the player named "John Holland" play for?
# Filters to the row(s) matching that exact name, pulls the Team column,
# and takes the first value with .iloc[0] (again guarding against
# multiple/zero matches returning something other than a plain string).
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# 8- What is the average salary of players, grouped by team?
# .groupby("Team").mean() averages every numeric column per team; then
# ["Salary"] picks out just the Salary averages as a Series indexed by
# team name.
result = df.groupby("Team").mean()["Salary"]

# 9- How many different teams are there?
# len() on a groupby object counts how many distinct groups (teams) exist.
result = len(df.groupby("Team"))
# .nunique() on the Team column gives the same count more directly, by
# counting distinct values.
result = df["Team"].nunique()

# 10- How many players does each team have?
# .value_counts() counts how many rows fall under each distinct Team
# value, sorted from most to fewest players.
result = df["Team"].value_counts()

# 11- Find the records where the name contains "and".
# Drop any row with missing data first, so the string check below doesn't
# choke on a NaN name.
df.dropna(inplace = True)
# result = df[df["Name"].str.contains("and")]
# A small helper function that checks (case-insensitively, via .lower())
# whether the substring "and" appears anywhere in a name -- e.g. this
# would match "Holland" (which contains "and") as well as any name
# literally containing the word "and".
def str_find(name):
    if "and" in name.lower():
        return True
    return False

# .apply(str_find) runs that helper on every value in the Name column,
# producing a boolean Series; using it to filter df keeps only the rows
# whose name matched.
result = df[df["Name"].apply(str_find)]

print(result)
