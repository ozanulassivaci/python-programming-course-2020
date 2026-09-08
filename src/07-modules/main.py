# "import mod" loads the local file mod.py (found in this same folder)
# as a module. Python runs mod.py's top-level code immediately when this
# import line executes -- that's why 'module loaded' (printed inside
# mod.py) appears in the output before anything from this file prints.
# Everything mod.py defines at the top level is now reachable through
# the mod.<name> dot syntax.
import mod

# Learned that a module's help() shows its docstrings and defined names.
# result = help(mod)
# help(mod) would print mod's module-level docstring plus a summary of
# every function/class/variable it defines, using their own docstrings
# where available.
# result = help(mod.func)
# help(mod.func) narrows that down to just func's own docstring and
# signature.

# Reading a plain variable defined in the module.
result = mod.number  # 10
# Reading a list defined in the module.
result = mod.numbers  # [1, 2, 3]
# mod.person is a dictionary defined in the module; square-bracket
# indexing with a key string reads one value out of it.
result = mod.person["name"]  # "Ali"
result = mod.person["age"]  # "25"
# Calling a function that lives inside the module. mod.func just prints
# its argument and returns None (there's no return statement in it), so
# `result` ends up being None right after this line.
result = mod.func(10)

# Classes defined inside a module are used the exact same way as classes
# defined locally: create an instance with mod.Person(), then call its
# methods on that instance.
p = mod.Person()
p.speak()

# `result` holds whatever the LAST assignment above produced, which is
# None (the return value of mod.func(10)), since mod.func doesn't
# explicitly return anything.
print(result)
