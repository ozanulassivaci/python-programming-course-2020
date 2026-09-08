'''
   info about this module
'''
# The triple-quoted string right at the top of the file (before any other
# code) is the module's DOCSTRING. Python treats it specially: it becomes
# this module's __doc__ attribute and is what help(mod) or dir(mod) would
# surface as the module's description. It's just a string literal, but
# its position (first statement in the file) is what gives it that
# special meaning.

# A "module" in Python is simply a .py file that can be imported by other
# files. When another file does "import mod" (see main.py in this same
# folder), Python runs this ENTIRE file top to bottom once, and then
# makes every name defined here (variables, functions, classes)
# accessible as mod.<name>. That's why the print() below actually runs
# and shows output the moment main.py imports this module -- importing a
# module executes its top-level code, it doesn't just "declare" things.
print('module loaded')

number = 10

numbers = [1, 2, 3]

person = {
    "name": "Ali",
    "age": "25",
    "city": "istanbul"
}

def func(x):
    '''
        info about this function
    '''
    # A docstring can also be the first statement inside a function; it
    # becomes that function's __doc__ and is what help(mod.func) shows.
    print(f'x: {x}')

class Person:
    def speak(self):
        print('I am speaking...')
