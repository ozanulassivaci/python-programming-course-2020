import pandas as pd

df = pd.read_csv("datasets/imdb.csv")

# 1- General info about the file.
result = df
result = df.columns
result = df.info

# 2- Show the first 5 records
result = df.head()

# 3- Show the first 10 records
result = df.head(10)

# 4- Show the last 5 records
result = df.tail()

# 5- Show the last 10 records
result = df.tail(10)

# 6- Take only the Movie_Title column.
result = df["Movie_Title"]

# 7- Take the first 5 records, only the Movie_Title column.
result = df["Movie_Title"].head()

# 8- Take the first 5 records, only Movie_Title and Rating columns.
result = df[["Movie_Title","Rating"]].head()

# 9- Take the last 7 records, only Movie_Title and Rating columns.
result = df[["Movie_Title","Rating"]].tail(7)

# 10- Take the second batch of 5 records, only Movie_Title and Rating columns.
result = df[5:20][["Movie_Title","Rating"]].head()

# 11- Take the first 50 records with an imdb rating of 8.0 or above,
#     only the Movie_Title and Rating columns.
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)


# 12- Get the titles of movies released between 2014 and 2015.
# Learning note: chaining boolean conditions with & needs each side wrapped in parentheses.
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]

# 13- List movies with more than 100,000 reviews (Num_Reviews) or an
#     imdb rating between 8 and 9.

result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]]

print(result)
print(df.columns)
