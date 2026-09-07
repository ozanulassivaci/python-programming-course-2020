import pandas as pd

df = pd.read_csv("datasets/youtube-ing.csv")

# 1- Get the first 10 records.
result = df.head(10)
# 2- Get the second group of 5 records.
result = df[5:20].head(5)
# 3- Find the column names in the dataset and how many there are.
result = df.columns
result = len(df.columns)
# 4- Drop the columns listed below and list the remaining columns.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
# 5- Find the average number of likes and dislikes.
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- Get the like and dislike columns for the first 50 videos.
result = df.head(50)[["title","likes","dislikes"]]

# 7- Which video has the most views?
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# 8- Which video has the fewest views?
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- Which are the top 10 most-viewed videos?
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- List the average likes per category, sorted.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Sort the comment counts per category from highest to lowest.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- How many videos are there in each category?
result = df["category_id"].value_counts()

# 13- Show the title length of each video in a new column.
df["title_len"] = df["title"].apply(len)

# 14- Show the number of tags used for each video in a new column.
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

def tag_count(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tag_count)

# 15- List the most popular videos (by like/dislike ratio).
# Learning note: had to guard against division by zero when both likes and dislikes are 0.

def calculate_like_dislike_ratio(dataset):
    likes_list = list(dataset["likes"])
    dislikes_list = list(dataset["dislikes"])

    pairs = list(zip(likes_list,dislikes_list))

    ratio_list = []

    for like,dislike  in pairs:
        if (like + dislike) == 0:
            ratio_list.append(0)
        else:
            ratio_list.append(like/(like+dislike))

    return ratio_list

df["like_ratio"] = calculate_like_dislike_ratio(df)

print(df.sort_values("like_ratio",ascending=False)[["title","likes","dislikes","like_ratio"]])
