mylist = [1, 2, 3]
# mystring = 'my string'

# print(len(mylist))
# print(len(mystring))
# print(type(mylist))
# print(type(mystring))
# The commented-out lines above are here for comparison: len() and
# type() already work "for free" on Python's own built-in types (list,
# str, ...) because those built-in classes already implement the special
# methods that len()/str()/etc. rely on internally. The Movie class
# below shows how YOUR OWN classes can plug into that same machinery.

# "Dunder" methods (short for "double underscore", because their names
# start and end with __) are special methods that Python calls
# automatically in certain situations -- you rarely call them directly
# yourself. Instead, built-in functions and operators (print(), str(),
# len(), +, ==, and many more) look for a matching dunder method on the
# object and call it behind the scenes. Defining these lets your custom
# classes behave like Python's own built-in types.
class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie object created.')

    # Learned that __str__ controls what print() shows for an object.
    # __str__ must return a string. Whenever code calls str(some_movie)
    # or print(some_movie), Python calls this method and uses whatever
    # string it returns, instead of the default
    # "<__main__.Movie object at 0x...>" representation you'd otherwise
    # get (see class.py in this same folder for that default look).
    def __str__(self):
        return f"{self.title} by {self.director}"

    # Learned that __len__ lets len() work on a custom object too.
    # Whenever code calls len(some_movie), Python calls this method and
    # uses its return value as the "length". Here it's repurposed to
    # mean the movie's duration in minutes, which is a bit of a
    # creative use of "length" but shows the mechanism clearly.
    def __len__(self):
        return self.duration

    # __del__ is the "destructor": Python calls it automatically right
    # before an object is destroyed and its memory is reclaimed
    # (garbage collected) -- normally when there are no more references
    # to it left. For a short script like this one, that typically ends
    # up happening as the program exits, which is why you'll see
    # 'movie object deleted' printed even though nothing in this file
    # explicitly deletes `m`.
    def __del__(self):
        print('movie object deleted')

# Creating the object runs __init__, which prints 'movie object created.'
# immediately.
m = Movie('movie title', 'director name', 120)

# print(str(mylist))
# str() on a built-in list just gives you its normal printed form, e.g.
# "[1, 2, 3]" -- lists don't need a custom __str__ for that, it's built
# into the list class already.
print(str(m))
# Calling str(m) triggers Movie.__str__(m), which returns
# "movie title by director name" (combining self.title and
# self.director) -- that's exactly what gets printed here.
# print(len(mylist))
# len(mylist) would return 3, the number of elements in the list.
# print(len(m))
# len(m) would call Movie.__len__(m), which returns self.duration (120)
# -- NOT the number of attributes or anything like that. This
# demonstrates that __len__ can return whatever number you decide is
# meaningful for your class.
