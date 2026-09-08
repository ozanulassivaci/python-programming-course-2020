# global scope
# A variable created at the top level of a file (not inside any function)
# lives in the "global scope" -- it's visible everywhere in the file,
# including inside functions, as long as those functions don't create
# their OWN variable with the same name.
x = 'global x'

def function():
    # local scope
    # x = 'local x'
    # If this line were uncommented, it would create a separate LOCAL
    # variable x that only exists inside `function`, and the print()
    # below would use THAT one instead, leaving the global x untouched.
    # With it commented out, Python looks for `x` locally first (LEGB:
    # Local, Enclosing, Global, Built-in, checked in that order), doesn't
    # find one, and falls back to the global x.
    print(x)

function()  # global x
print(x)    # global x -- unaffected either way, since function() never
            # actually modified anything, it only read the value

####################

# global
name = 'Kerem'

def change_name(new_name):
    # local
    # Normally, assigning to a name inside a function (like `name = ...`)
    # creates a new LOCAL variable, even if a global variable of the same
    # name already exists -- it does NOT automatically modify the global
    # one. The `global` keyword overrides that default: it tells Python
    # "when I assign to `name` in this function, modify the global
    # variable directly, don't create a local shadow of it."
    global name
    name = new_name
    print(name)

change_name('Ada')  # prints Ada, and also updates the global `name`
print(name)  # Ada -- the global variable really was changed

####################

name = 'global string'

def greeting():
    # name = 'Kerem'
    # If this were uncommented, `hello()` (defined below, inside
    # `greeting`) would see THIS local `name` instead of the global one,
    # because it sits in the "enclosing" scope, which LEGB checks before
    # falling back to global.

    def hello():
        # name = 'Ada'
        # A function can be defined inside another function -- this
        # inner `hello` only exists while `greeting` is running, and it
        # can see variables from `greeting`'s scope (its "enclosing"
        # scope), not just the global scope.
        print('hello ' + name)

    hello()

# Since neither the `name = 'Kerem'` line in greeting() nor the
# `name = 'Ada'` line in hello() is actually active, `hello()` falls all
# the way back to the global `name`, printing 'hello global string'.
greeting()

####################

x = 50
def test():
    # Declaring `global x` up front means EVERY use of `x` in this
    # function -- both reading and writing -- refers to the global
    # variable, not a local one. That's why the print() below can read
    # the CURRENT global value (50) even though the very next line is
    # about to reassign it.
    global x
    print(f'x : {x}')  # 50 -- reads the global value before it's changed

    x = 100  # this reassigns the GLOBAL x, thanks to `global x` above
    print(f'changed x to {x}')  # 100

test()
print(x)  # 100 -- the global variable was permanently changed by test()
