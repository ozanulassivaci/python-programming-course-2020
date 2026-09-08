# Method 1
# import math
# import math as calc
# "import math" gives access to everything in the math module, but only
# through the "math." prefix (math.sqrt(), math.factorial(), ...). You
# can also rename the module while importing it -- "import math as calc"
# -- which lets you use "calc." instead, useful for shortening long
# module names or avoiding a name clash.

# value = dir(math)
# dir(math) would list every name (function/constant) the math module
# provides, e.g. sqrt, factorial, floor, ceil, pi, and many more.
# value = help(math)
# help(math) prints the module's full documentation.
# value = help(math.factorial)
# help(math.factorial) narrows that down to just this one function.
# value = math.sqrt(49)
# math.sqrt(x) returns the square root of x as a float: sqrt(49) = 7.0.
# value = math.factorial(5)
# math.factorial(x) returns x! (x factorial), i.e. x * (x-1) * ... * 1:
# factorial(5) = 5*4*3*2*1 = 120.
# value = math.floor(5.9)
# math.floor(x) rounds DOWN to the nearest whole number: floor(5.9) = 5.
# value = math.ceil(5.9)
# math.ceil(x) rounds UP to the nearest whole number: ceil(5.9) = 6.

# value = calc.factorial(5)
# Same as math.factorial(5) above, just using the "calc" alias instead.

# Method 2
# from math import *
# This form imports every public name from the math module directly into
# this file's own namespace, so you could call sqrt(49) instead of
# math.sqrt(49) -- no prefix needed. It's generally discouraged in real
# projects because it makes it hard to tell, just by reading the code,
# which module a given name came from, and it can silently overwrite
# names you already defined (exactly the gotcha demonstrated below).

# This is a LOCAL function named sqrt, defined before any import
# statement touches that name.
def sqrt(x):
    print('x :' + str(x))

# Learned that a local function/import can shadow a name from the standard library.
# "from math import factorial, sqrt, ceil" imports these three specific
# names from the math module directly into this file. This line runs
# AFTER the "def sqrt(x)" above, and import statements simply create (or
# overwrite) a name binding in the current namespace -- so this import
# REPLACES the local sqrt function defined above with math's own sqrt
# function. From this point on in the file, the name "sqrt" refers to
# math.sqrt, not the print-based function that used to have that name.
from math import factorial, sqrt, ceil

# value = factorial(5)
# factorial(5) would return 120 (5*4*3*2*1), using the name imported
# straight from the math module.
# Because sqrt was overwritten by the import above, this calls
# math.sqrt(9), NOT the local "def sqrt(x): print(...)" version -- so it
# returns a number (3.0) instead of printing "x :9" and returning None.
value = sqrt(9)
# value = ceil(9.8)
# ceil(9.8) would return 10, rounding up to the next whole number.

# Prints 3.0 -- the float square root of 9, coming from math.sqrt.
print(value)
