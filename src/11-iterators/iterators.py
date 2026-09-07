# numbers = [1,2,3,4,5]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# for i in numbers:
#     print(i)

# numbers = [1,2,3,4,5]
# iterator = iter(numbers)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

# Building my own iterable by defining __iter__ and __next__ instead of using a builtin.
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

number_range = MyNumbers(20,50)

myiter = iter(number_range)

# print(next(myiter))
# print(next(myiter))

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break


# for x in number_range:
#     print(x)

