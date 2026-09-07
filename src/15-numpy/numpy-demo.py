import numpy as np

# 1- Create a numpy array with values (10,15,30,45,60).
result = np.array([10,15,30,45,60])

# 2- Create a numpy array with numbers between 5 and 15.
result = np.arange(5,15)

# 3- Create a numpy array from 50 to 100, stepping by 5.
result = np.arange(50,100,5)

# 4- Create an array of 10 zeros.
result = np.zeros(10)

# 5- Create an array of 10 ones.
result = np.ones(10)

# 6- Generate 5 evenly spaced numbers between 0 and 100.
result = np.linspace(0,100,5)

# 7- Generate 5 random integers between 10 and 30.
result = np.random.randint(10,30,5)

# 8- Generate 10 random numbers (roughly between -1 and 1).
result = np.random.randn(10)

# 9- Create a (3x5) matrix with random values between 10 and 50.
# result = np.random.randint(10,50,15).reshape(3,5)

# 10- What are the row and column totals of the generated matrix?
# Learning note: reshape lets me turn a flat array into a matrix without copying data.
matrix = np.random.randint(-50,50,15).reshape(3,5)
print(matrix)
# row_total = matrix.sum(axis = 1)
# col_total = matrix.sum(axis = 0)
# print(matrix)
# print(row_total)
# print(col_total)

# 11- What are the max, min and mean of the generated matrix?
result = matrix.max()
result = matrix.min()
result = matrix.mean()

# 12- What is the index of the largest value in the matrix?
result = matrix.argmax()
result = matrix.argmin()

# 13- Select the first 3 elements of an array containing numbers 10 to 20.
arr = np.arange(10,20)
print(arr)

result = arr[:3]

# 14- Print the elements of the array in reverse order.
result = arr[::-1]

# 15- Select the first row of the matrix.
result = matrix[0]

# 16- Which element is in row 2, column 3 of the matrix?
result = matrix[1,2]

# 17- Select the first element of every row in the matrix.
result = matrix[:,0]

# 18- Square every element of the matrix.
result = matrix ** 2

# 19- Which elements of the matrix are positive even numbers?
#     Use a range of (-50, +50).
# Learning note: boolean masking (matrix[condition]) still feels like magic compared to writing a loop.
evens = matrix[matrix % 2 == 0]
result = evens[evens>0]

print(result)
