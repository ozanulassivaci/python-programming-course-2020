# 1-  Create a list with elements "Bmw, Mercedes, Opel, Mazda".
cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# 2-  How many elements does the list have?
result = len(cars)
# 3-  What are the first and last elements of the list?
result = cars[0]
result = cars[3]
result = cars[-1]
# 4-  Replace Mazda with Toyota.
# cars[-1] = 'Toyota'
result = cars
# 5-  Is Mercedes an element of the list?
result = 'Mercedes' in cars
# 6-  What is the value at index -2?
result = cars[-2]
# 7-  Get the first 3 elements of the list.
result = cars[0:3]
result = cars[:3]
result = cars[-2:]
# 8-  Replace the last 2 elements with "Toyota" and "Renault".
cars[-2:] = ['Toyota', 'Renault']
result = cars
# 9-  Append "Audi" and "Nissan" to the list.
result = cars + ['Audi', 'Nissan']
# 10- Remove the last element of the list.
del cars[-1]
result = cars
# 11- Print the list elements in reverse.
result = cars[::-1]
# 12- Store the following data in a list.

      # studentA: Yigit Bilgi 2010, (70,60,70)
      # studentB: Sena Oznur  1999, (80,80,70)
      # studentC: Ahmet Aykut 1998, (80,70,90)

studentA = ['Yigit', 'Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Oznur', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Aykut', 1998, [80, 70, 90]]

# 13- Print the list elements.

result = studentA[0]
result = studentB[1]
# studentA[3][1] because the grades themselves are a list nested inside the list
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} is {2019-studentA[2]} years old with a grade average of {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)
