names = ['Ali', 'Yagmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  Add "Cenk" to the end of the list.
# names.append('Cenk')

# 2-  Add "Sena" to the front of the list.
# names.insert(0, 'Sena')
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')

# 3-  Remove "Deniz" from the list.
# names.remove('Deniz')
# names.pop()
# names.pop(1)

# 4-  What is the index of "Deniz"?
# index = names.index('Deniz')
# names.pop(index)

# 5-  Is "Ali" an element of the list?
# result = 'Ali' in names
# result = names.index('Ali')

# 6-  Reverse the list elements.
# names.reverse()

# 7-  Sort the list elements alphabetically.
# names.sort()

# 8-  Sort the years list numerically.
# years.sort()

# 9-  Turn the string "Chevrolet,Dacia" into a list.
# text = "Chevrolet,Dacia"
# result = text.split(',')

# 10- What are the min and max values in years?
# smallest = min(years)
# largest = max(years)
# print(smallest, largest)

# 11- How many times does 1998 appear in years?
# result = years.count(1998)

# 12- Clear every element from years.
# years.clear()

# 13- Store 3 car brands entered by the user in a list.

brands = []

# Learned that append() only adds one item at a time - extend() is
# the one you'd want for merging whole lists together.
brand = input("brand: ")
brands.append(brand)

brand = input("brand: ")
brands.append(brand)

brand = input("brand: ")
brands.append(brand)

print(brands)
