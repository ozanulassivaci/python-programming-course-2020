'''
    Circle Area      : pi*r^2
    Circle Perimeter : 2*pi*r

    * Given the radius of a circle, calculate its area and
    perimeter. (r: 3.14)
'''

pi = 3.14

# input() always returns a string, even if the user types digits. float()
# converts that text into a real floating-point number so it can be used
# in arithmetic -- trying to do math directly on the string from input()
# would either fail (for *, ** with another number it actually works
# oddly) or behave unexpectedly, so converting explicitly is the safe habit.
r = float(input("radius: "))

# ** is the exponentiation operator: r ** 2 means "r squared" (r to the
# power of 2). Multiplying two floats (pi and r**2) produces another float.
area = pi * (r ** 2)
print(type(area))  # <class 'float'>

perimeter = 2 * pi * r
print(type(perimeter))  # <class 'float'>

# "+" can't mix strings and numbers directly, so str() converts area and
# perimeter into text first, letting them be concatenated into one string.
print("area: " + str(area) + " perimeter: " + str(perimeter))
