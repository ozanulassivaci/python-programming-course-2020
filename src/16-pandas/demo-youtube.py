import pandas as pd

# Load a dataset of trending YouTube videos (title, views, likes,
# dislikes, category_id, tags, etc.) from CSV.
df = pd.read_csv("datasets/youtube-ing.csv")

# 1- Get the first 10 records.
result = df.head(10)
# 2- Get the second group of 5 records.
# df[5:20] slices rows by position (indices 5 through 19), and .head(5)
# then takes just the first 5 of that slice -- i.e. rows 5 through 9,
# "the second batch of 5" after the first 5 rows (0-4).
result = df[5:20].head(5)
# 3- Find the column names in the dataset and how many there are.
result = df.columns
result = len(df.columns)
# 4- Drop the columns listed below and list the remaining columns.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
# .drop(list, axis=1, inplace=True) removes several columns at once by
# name, modifying df directly instead of returning a new DataFrame.
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)
# 5- Find the average number of likes and dislikes.
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- Get the like and dislike columns for the first 50 videos.
# .head(50) takes the first 50 rows, then the column list narrows down to
# just title/likes/dislikes.
result = df.head(50)[["title","likes","dislikes"]]

# 7- Which video has the most views?
# df["views"].max() == df["views"] builds a boolean mask that's True only
# where a row's views equal the overall maximum. Filtering df with it
# keeps that row (or rows, in case of a tie), pulls the title, and
# .iloc[0] grabs the first match as a plain value.
result = df[df["views"].max() == df["views"]]["title"].iloc[0]

# 8- Which video has the fewest views?
# Same pattern as above, but comparing against the minimum instead.
result = df[df["views"].min() == df["views"]]["title"].iloc[0]

# 9- Which are the top 10 most-viewed videos?
# .sort_values("views", ascending=False) orders rows from most-viewed to
# least, .head(10) takes the top 10, then the column list narrows to
# title/views only.
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- List the average likes per category, sorted.
# Groups rows by category_id, averages every numeric column per group,
# picks out the "likes" average, then .sort_values("likes") on the
# GROUPED dataframe (before selecting "likes") sorts categories by their
# average likes ascending.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Sort the comment counts per category from highest to lowest.
# .sum() per category totals up comment_count, then sorting descending
# shows the category with the most total comments first.
result = df.groupby("category_id").sum().sort_values("comment_count", ascending = False)["comment_count"]

# 12- How many videos are there in each category?
result = df["category_id"].value_counts()

# 13- Show the title length of each video in a new column.
# .apply(len) runs Python's built-in len() on every title string,
# creating a new "title_len" column with each video's character count.
df["title_len"] = df["title"].apply(len)

# 14- Show the number of tags used for each video in a new column.
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))

# The "tags" column stores multiple tags in one string, separated by "|"
# characters. Splitting on "|" turns that string into a list of
# individual tags, and len() on that list counts how many tags there are.
def tag_count(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tag_count)

# 15- List the most popular videos (by like/dislike ratio).
# Learning note: had to guard against division by zero when both likes and dislikes are 0.

# A custom function to compute each video's "approval ratio":
# likes / (likes + dislikes). Written as a plain loop over parallel lists
# rather than a vectorized pandas expression, mainly to make the
# divide-by-zero guard easy to read.
def calculate_like_dislike_ratio(dataset):
    likes_list = list(dataset["likes"])
    dislikes_list = list(dataset["dislikes"])

    # zip() pairs up the two lists element-by-element: the first like
    # count with the first dislike count, the second with the second, and
    # so on -- turning two parallel lists into one list of (like, dislike)
    # tuples.
    pairs = list(zip(likes_list,dislikes_list))

    ratio_list = []

    for like,dislike  in pairs:
        # If a video has NO likes and NO dislikes at all, likes+dislikes
        # would be 0, and dividing by 0 would crash the program. This
        # guard treats that edge case as a ratio of 0 instead of erroring
        # out.
        if (like + dislike) == 0:
            ratio_list.append(0)
        else:
            ratio_list.append(like/(like+dislike))

    return ratio_list

# Running the helper over the whole DataFrame and storing the results as
# a new "like_ratio" column -- one ratio per video, aligned by row order.
df["like_ratio"] = calculate_like_dislike_ratio(df)

# Sorting by that new column, descending, surfaces the videos with the
# highest approval ratio (proportionally more likes than dislikes) at the
# top; narrowing to the relevant columns for a clean printout.
print(df.sort_values("like_ratio",ascending=False)[["title","likes","dislikes","like_ratio"]])
