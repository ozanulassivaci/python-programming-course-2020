import random

# result = dir(random)
# result = help(random)

result = random.random()  # 0.0 - 1.0
result = random.random() * 100
result = int(random.uniform(10, 100))
result = random.randint(1, 100)

greeting = 'hello there'
names = ['ali', 'yagmur', 'deniz', 'cenk', 'ahmet', 'efe']
# result = names[random.randint(0,len(names)-1)]

result = random.choice(names)
result = random.choice(greeting)

# Learned that shuffle() reorders a list in place and returns None.
numbers = list(range(10))
random.shuffle(numbers)
result = numbers

numbers = range(100)
result = random.sample(numbers, 3)
result = random.sample(names, 2)

print(result)
