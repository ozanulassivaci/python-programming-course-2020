import matplotlib.pyplot as plt
import numpy as np

# np.linspace(-10,9,20) creates 20 evenly spaced x-values from -10 up to 9
# inclusive.
x = np.linspace(-10,9,20)
# y = x**3 is a cubic curve: negative for negative x, positive for
# positive x, crossing zero at x=0, and growing/shrinking much faster than
# x itself as you move away from 0.
y = x ** 3
# z = x**2 is a parabola (a "square" curve): always non-negative (squaring
# a negative number makes it positive), with its minimum (0) at x=0 and
# rising symmetrically on both sides.
z = x ** 2

"""
# This example shows the low-level, most flexible way to place plots: you
# create a bare Figure (the overall canvas/window) and then manually add
# "Axes" (individual plot areas) to it at exact positions.
figure = plt.figure()
# .add_axes([left, bottom, width, height]) places a new set of axes on the
# figure using RELATIVE coordinates from 0 to 1 (fractions of the figure's
# total width/height) -- (0,0) is the bottom-left corner of the figure and
# (1,1) is the top-right. Here: start 10% in from the left, 10% up from
# the bottom, and take up 80% of the width and 80% of the height -- i.e. a
# large plot filling most of the figure.
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])

# 'b' is a shorthand format string for a solid blue line.
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

# A SECOND, smaller set of axes placed on the SAME figure: starting 15%
# from the left, 60% up from the bottom, and only 25% wide / 25% tall --
# this creates a small "inset" plot layered in the upper-left area of the
# same figure, overlapping the big plot's space. This manual add_axes
# approach is how you'd build an inset chart (a small zoomed detail plot
# sitting inside a bigger one).
axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")

"""
"""
figure = plt.figure()

# Axes covering the ENTIRE figure (0,0 to 1,1 -- the full width and
# height), so this one set of axes fills the whole window.
axes = figure.add_axes([0,0,1,1])

# Plotting both curves on the SAME axes overlays them on one chart rather
# than giving each its own subplot.
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
# loc=4 places the legend box in a specific fixed corner: matplotlib's
# legend location codes number the corners/positions (4 = "lower right").
# Using a numeric code like this is an alternative to strings such as
# loc="upper left".
axes.legend(loc=4)
"""

# Learning note: plt.subplots() is a lot less fiddly than manually placing axes with add_axes().
# plt.subplots(nrows, ncols, figsize=(w,h)) is the easier, higher-level
# way to get a grid of axes -- it creates the figure AND the axes together
# in one call, arranged in a regular grid, so you don't have to hand-place
# each one with fractional coordinates like add_axes() requires. Here:
# 2 rows, 1 column (two plots stacked vertically), and figsize sets the
# overall figure size in inches (8 inches wide by 8 inches tall).
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))

# With nrows=2, ncols=1, `axes` is a 1D array of 2 axes objects -- index
# them like a list: axes[0] is the top plot, axes[1] is the bottom plot.
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

# Prevents the two subplots' titles/labels from overlapping each other.
plt.tight_layout()
# fig.savefig(path) writes the current figure out to a file on disk. The
# file extension (.pdf here) tells matplotlib which format to save in --
# it also supports .png, .jpg, .svg, etc. This saves a copy even before
# (or instead of) displaying it interactively.
fig.savefig("figure2.pdf")

# Displays the figure in an interactive window/inline output.
plt.show()
