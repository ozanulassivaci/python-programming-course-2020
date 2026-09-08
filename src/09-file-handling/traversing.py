# Learned that seek(0) resets the cursor back to the start of the file.
# "with open(...) as file:" is a CONTEXT MANAGER. It opens the file,
# hands it to you as `file` for the duration of the indented block, and
# then automatically calls file.close() for you when the block ends --
# even if an exception happens partway through. This is the recommended
# way to work with files in Python, since you can't forget to close them.
with open("newfile.txt", "r", encoding="utf-8") as file:
    # Reads the first 10 characters from the file, starting at the
    # cursor's initial position (the very start of the file, position 0).
    # This also moves the cursor forward by 10.
    content = file.read(10)
    print(content)
    # file.seek(0) moves the cursor back to position 0 -- the very
    # beginning of the file -- regardless of where it currently is. This
    # is the tool that lets you re-read (or re-write) from the start
    # without closing and reopening the file.
    file.seek(0)
    # file.tell() returns the cursor's CURRENT position as a number of
    # characters/bytes from the start of the file. Since we just called
    # seek(0), this prints 0.
    print(file.tell())
    # Because the cursor was reset to the start, this reads the exact
    # same first 10 characters as `content` did above -- so content2
    # ends up equal to content, even though we already "used up" that
    # part of the file once.
    content2 = file.read(10)
    print(content2)
