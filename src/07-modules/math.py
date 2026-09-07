# Method 1
# import math
# import math as calc

# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# value = calc.factorial(5)

# Method 2
# from math import *

def sqrt(x):
    print('x :' + str(x))

# Learned that a local function/import can shadow a name from the standard library.
from math import factorial, sqrt, ceil

# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)

print(value)
