import matplotlib.pyplot as plt

# This file is a tour of several different matplotlib CHART TYPES, each
# wrapped in its own triple-quoted string so only one example runs "live"
# at a time (Python treats a bare triple-quoted string as a no-op
# statement -- effectively a multi-line comment -- so none of the code
# inside these blocks currently executes).

"""
# Stack Plot
# A stack plot shows several series "stacked" on top of one another, so
# the total height of the stack at any point represents the combined sum
# of all series at that point -- useful for seeing both individual
# contributions and the overall total over time.
year = [2011,2012,2013,2014,2015]

player1 = [8,10,12,7,9]
player2 = [7,12,5,15,21]
player3 = [18,20,22,25,19]


# plt.plot([],[], color=..., label=...) is a small trick: it plots
# NOTHING (empty x and y lists), purely so that a colored, labeled entry
# shows up in the legend. This is needed because plt.stackplot() itself
# doesn't automatically create legend entries the way plt.plot() does, so
# these three "invisible" plots are a workaround to get a proper legend
# with each player's color and name.
plt.plot([],[],color="y",label="player1")
plt.plot([],[],color="r",label="player2")
plt.plot([],[],color="b",label="player3")

# plt.stackplot(x, y1, y2, y3, colors=[...]) draws the actual stacked
# area chart: for each year, player1's goals form the bottom band, then
# player2's goals are stacked on top of that, then player3's on top of
# that -- so the top edge of the whole stack at each year shows the
# combined total goals from all three players that year.
plt.stackplot(year,player1,player2,player3, colors=["y","r","b"])
plt.title("Goals scored by year")
plt.xlabel("year")
plt.ylabel("Goal count")
plt.legend()
plt.show()

"""


"""
Pie Chart

# A pie chart shows each category as a "slice" of a circle, with each
# slice's angle (and area) proportional to its share of the total.
goal_types = 'Penalty','Shot on target','Free kick'

goals = [12,35,7]
colors = ['y','r','b']

# plt.pie(values, labels=..., colors=..., shadow=True, explode=(...), autopct=...)
# - values (goals) determines each slice's size, proportional to the sum
#   of all values (12+35+7 = 54 total, so "Shot on target" at 35 would be
#   the largest slice, roughly 35/54 ~= 65% of the pie).
# - labels names each slice.
# - shadow=True adds a drop-shadow effect for visual depth.
# - explode=(0.05,0.05,0.05) offsets each slice slightly outward from the
#   pie's center (by that fraction of the radius) -- a small, equal
#   "explode" on every slice here, though explode is often used with
#   different values per slice to emphasize just one.
# - autopct="%1.1f%%" auto-labels each slice with its percentage of the
#   whole, formatted to 1 decimal place (e.g. "64.8%") -- the %% is an
#   escaped literal percent sign in Python's old-style string formatting.
plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()


"""
"""
Bar Chart

# Learning note: two slightly offset x positions per bar group is how you get bars side by side instead of stacked.
# plt.bar(x_positions, heights, label=..., width=...) draws vertical bars
# at the given x positions with the given heights. To show TWO bars
# side-by-side per "day" (instead of one bar overwriting the other at the
# same x position), each series uses x positions offset by half a bar
# width from the other: BMW's bars sit at 0.25, 1.25, 2.25... and Audi's
# sit at 0.75, 1.75, 2.75... With width=.5 for both, this places each
# pair of bars (BMW then Audi) snugly next to each other, centered around
# whole numbers like 0.5, 1.5, 2.5 -- giving a classic grouped/clustered
# bar-chart look rather than bars stacked on top of each other.
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Day")
plt.ylabel("Distance (km)")
plt.title("Vehicle info")
"""

"""
Histogram
# A histogram groups continuous numeric data into "bins" (ranges) and
# shows how many data points fall into each bin as a bar -- unlike a
# regular bar chart, it's meant for showing the DISTRIBUTION/frequency of
# a single numeric variable, not comparing separate named categories.
ages = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
# The bin EDGES: this defines 10 bins of width 10 each (0-10, 10-20, ...,
# 90-100) -- note ages above 100 would fall outside the last defined bin
# edge (100), so matplotlib would either clip or extend them depending on
# version/settings.
age_groups = [0,10,20,30,40,50,60,70,80,90,100]

# plt.hist(data, bins, histtype="bar", rwidth=0.8) counts how many ages
# fall into each of the bins defined by age_groups, and draws one bar per
# bin whose HEIGHT is that count. rwidth=0.8 shrinks each bar to 80% of
# its available bin width, leaving a small visible gap between
# neighboring bars for readability. Looking at `ages`, you'd expect the
# 40-50 and 50-60 bins to be tall (several values cluster around 42-55),
# since histograms make it easy to spot where a dataset's values
# concentrate.
plt.hist(ages,age_groups,histtype="bar",rwidth=0.8)
plt.xlabel("age groups")
plt.ylabel("Number of people")
plt.title("Histogram")
"""

plt.show()
