import matplotlib.pyplot as plt
import numpy as np

# matplotlib is the standard Python library for drawing charts/plots.
# pyplot (imported here as plt, the near-universal convention) is its
# "quick and easy" interface: it keeps track of a current figure and axes
# behind the scenes so you can just call functions like plt.plot(),
# plt.title(), plt.show() without explicitly managing those objects
# yourself. This file walks through several examples; only ONE of them is
# "live" (not wrapped in a triple-quoted string, which Python treats as a
# no-op string literal, effectively commenting out the whole block) at a
# time, so you can flip between them to see different matplotlib features.

""" Example 1 ***
x = [1,2,3,4]
y = [1,4,9,16]

# plt.plot(x, y, format_string) draws x vs y as a line/marker plot. The
# format_string "o--r" is shorthand for: 'o' = circle markers at each data
# point, '--' = a dashed line connecting them, 'r' = red color. So this
# draws red circles at (1,1),(2,4),(3,9),(4,16) connected by a red dashed
# line.
plt.plot(x,y,"o--r")
# plt.axis([xmin,xmax,ymin,ymax]) manually sets the visible range of both
# axes, instead of letting matplotlib auto-scale to fit the data.
plt.axis([0,6,0,20])

# These add text labels to the chart: an overall title, and labels for
# the x and y axes, so a viewer knows what they're looking at.
plt.title("Chart Title")
plt.xlabel("x label")
plt.ylabel("y label")
# plt.show() renders the figure in a window (or inline, in a notebook).
# Nothing is actually displayed until this is called.
plt.show()
"""

""" Example 2 ***"""
# Learning note: plt.legend() only shows labels for plots that were given a label=... argument.
# np.linspace(0,2,100) creates 100 evenly spaced x-values between 0 and 2
# inclusive -- a smooth, dense set of points so the resulting curves look
# continuous rather than jagged.
x = np.linspace(0,2,100)

# Each plt.plot() call here draws one curve on the SAME figure (pyplot
# keeps reusing the current figure/axes until you explicitly create a new
# one or call plt.show()). label="..." attaches a name to that curve
# specifically so plt.legend() (below) can show it in the legend box.
# y = x is a straight diagonal line (linear).
plt.plot(x, x, label="linear",color="red")
# y = x**2 curves upward faster than linear (quadratic growth).
plt.plot(x, x**2, label="quadratic",color="yellow")
# y = x**3 curves upward even faster still (cubic growth) -- for x
# between 0 and 2, you'd see cubic overtake quadratic which overtakes
# linear as x grows.
plt.plot(x, x**3, label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("simple plot")
# plt.legend() draws a small box on the chart listing each curve's label
# next to a sample of its line style/color, so viewers can tell the three
# curves apart. It only picks up curves that were plotted WITH a
# label=... argument -- any plot() call without one is simply left out of
# the legend.
plt.legend()

plt.show()


""" Example 3 ***
x = np.linspace(0,2,100)
# plt.subplots(n) creates a figure containing n separate, stacked
# "axes" (individual plot areas) all at once, instead of one shared plot.
# It returns a tuple: (the overall figure object, an array of the axes).
# With a single integer argument like 3, `axs` is a 1D array of 3 axes,
# indexable like axs[0], axs[1], axs[2].
fig,axs =  plt.subplots(3)

# Each axes object has its OWN .plot()/.set_title() methods -- this is
# the "object-oriented" matplotlib style (as opposed to the plt.plot()
# convenience style above), which is more explicit about which subplot
# you're drawing into.
axs[0].plot(x, x, color="red")
axs[0].set_title("linear")

axs[1].plot(x, x**2, color="green")
axs[1].set_title("quadratic")

axs[2].plot(x, x**3, color="yellow")
axs[2].set_title("cubic")

# plt.tight_layout() automatically adjusts spacing between subplots so
# titles/labels don't overlap each other -- good practice whenever you
# have multiple subplots.
plt.tight_layout()

plt.show()

"""

""" Example 4 ***

x = np.linspace(0,2,100)
# plt.subplots(2,2) creates a 2x2 GRID of axes (4 subplots total). Because
# both dimensions are given, `axs` becomes a 2D array indexed as
# axs[row,col], mirroring how you'd index a numpy matrix.
fig,axs =  plt.subplots(2,2)
# fig.suptitle() sets one title for the WHOLE figure (covering all
# subplots), distinct from each individual axes' own .set_title().
fig.suptitle("chart title")

axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="blue")
axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="yellow")

plt.show()
"""

""" Example 5 ***
import pandas as pd

df = pd.read_csv("nba.csv")

# Drops the "Number" column (jersey number, not meaningful to average),
# then groups the remaining rows by Team and averages every numeric
# column per team -- exactly the pandas groupby pattern from the pandas
# lessons, just feeding into a plot here instead of being printed.
df = df.drop(["Number"], axis = 1).groupby("Team").mean()

# pandas DataFrames have a convenient .plot() method that hands off to
# matplotlib automatically. subplots=True draws EACH column of df.head()
# (the first 5 teams, after groupby+mean) as its own separate subplot,
# instead of overlaying them all on one chart.
df.head().plot(subplots=True)
plt.legend()
plt.show()

"""
