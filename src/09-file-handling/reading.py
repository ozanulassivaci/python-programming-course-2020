# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("file reading error")
# finally:
#     print("file closed.")
#     file.close()
# Opening a file that doesn't exist in "r" mode raises FileNotFoundError,
# which this try/except is ready to catch. Printing `file` itself (if
# the open succeeded) would show something like
# "<_io.TextIOWrapper name='newfile2.txt' mode='r' ...>" -- the file
# OBJECT, not its contents; you still need to call read()/readline()/etc.
# to get the actual text. Note this particular example has a bug: if
# FileNotFoundError is raised, `file` was never successfully assigned,
# so the file.close() inside `finally` would itself raise a NameError --
# a good illustration of why cleanup code in `finally` needs to be
# written carefully.

# Opening "newfile.txt" for reading. Since no mode argument's absence is
# relied on here (mode is explicit), and no error handling wraps this
# call, this line would raise FileNotFoundError if newfile.txt didn't
# exist -- but it does exist in this folder, so this succeeds and gives
# us a file object to read from below.
file = open("newfile.txt", "r", encoding="utf-8")

# ********** for loop

# for i in file:
#     print(i, end="")
# A file object is "iterable": looping over it with a for loop hands you
# one line at a time (including the trailing "\n" newline character
# still attached to each line, if the file has one). Passing end="" to
# print() stops print() from adding ANOTHER newline of its own on top of
# the one already in the line, so lines don't end up double-spaced.

# ********** read() function

# content1 = file.read()
# file.read() with no argument reads and returns the ENTIRE remaining
# content of the file, from wherever the cursor currently is, as one
# single string (newlines included as literal "\n" characters inside
# it).

# print("content 1")
# print(content1)

# content2 = file.read()
# Every read (or readline/readlines) call moves an internal "cursor"
# forward through the file, tracking how far you've already read. Once
# read() has consumed everything up to the end of the file, the cursor
# sits at the very end, so calling read() again returns an EMPTY STRING
# ('') -- there's nothing left to read, not an error.

# print("content 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)
# Passing a number to read(n) limits it to reading at most n CHARACTERS
# from the current cursor position, then stops -- the cursor moves
# forward by n each time. So three calls like this (5, then 3, then 3)
# read three separate, consecutive chunks of the file, 5 then 3 then 3
# characters long, continuing from where the previous call left off.

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
# file.readline() reads and returns just ONE line at a time (up to and
# including its newline character), moving the cursor to the start of
# the next line each time it's called. Calling it repeatedly like this
# walks through the file line by line. Once past the last line, it
# returns an empty string, same idea as read() running dry.

# ********** readlines() function

# Learned that read() called twice in a row returns an empty string the
# second time, because the file cursor already moved to the end.
# lines = file.readlines()
# file.readlines() reads the ENTIRE remaining file at once, but instead
# of returning it as a single string like read() does, it splits it into
# a LIST of strings, one per line (each still ending in "\n" where the
# original file had a line break).

# print(lines[0])
# print(lines[1])
# print(lines[2])
# Indexing into that list with [0], [1], [2] prints the first, second,
# and third lines of the file respectively.

# Always close a file when you're done with it, to release the
# operating system resources it's holding and make sure any buffered
# data is flushed. (The "with" statement used in the other files in this
# folder does this automatically, even if an error happens partway
# through -- see traversing.py and updating.py for that pattern.)
file.close()
