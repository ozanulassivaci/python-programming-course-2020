# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("file reading error")
# finally:
#     print("file closed.")
#     file.close()

file = open("newfile.txt", "r", encoding="utf-8")

# ********** for loop

# for i in file:
#     print(i, end="")

# ********** read() function

# content1 = file.read()

# print("content 1")
# print(content1)

# content2 = file.read()

# print("content 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

# print(content)

# ********** readline() function

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# ********** readlines() function

# Learned that read() called twice in a row returns an empty string the
# second time, because the file cursor already moved to the end.
# lines = file.readlines()

# print(lines[0])
# print(lines[1])
# print(lines[2])

file.close()
