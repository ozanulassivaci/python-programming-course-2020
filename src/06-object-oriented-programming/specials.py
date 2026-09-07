mylist = [1, 2, 3]
# mystring = 'my string'

# print(len(mylist))
# print(len(mystring))
# print(type(mylist))
# print(type(mystring))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie object created.')

    # Learned that __str__ controls what print() shows for an object.
    def __str__(self):
        return f"{self.title} by {self.director}"

    # Learned that __len__ lets len() work on a custom object too.
    def __len__(self):
        return self.duration

    def __del__(self):
        print('movie object deleted')

m = Movie('movie title', 'director name', 120)

# print(str(mylist))
print(str(m))
# print(len(mylist))
# print(len(m))
