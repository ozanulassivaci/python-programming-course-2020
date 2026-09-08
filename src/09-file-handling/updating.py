# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("test")
# "r+" mode opens a file for BOTH reading and writing, WITHOUT erasing
# its existing content the way "w" would. file.seek(20) moves the cursor
# to character position 20, and file.write("test") then OVERWRITES the
# characters starting at that position with "test" -- it does NOT insert
# "test" and push the rest of the file forward. This is a common
# surprise for beginners: writing in the middle of a file in "r+" mode
# replaces existing characters one-for-one, it doesn't make room for new
# ones.

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())
# Just reading and printing the whole file again afterward, to see the
# effect of the overwrite above.

# ***** Update at the end of the file *****

# with open("newfile.txt","a", encoding="utf-8") as file:
#     file.write("\nOznur")
# Appending is the easy, safe way to add content: "a" mode always writes
# at the end, regardless of where a cursor would otherwise be, and never
# touches or overwrites what's already there.

# ***** Update at the start of the file *****

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Aykut\n" + content
#     file.seek(0)
#     file.write(content)
# Since there's no way to directly "insert" text at the beginning of a
# file on disk, the trick is: read the WHOLE existing content into a
# string, build a new string with your new text stuck on the front
# (string concatenation with +), seek back to position 0, and write the
# whole new combined string out. This works but re-writes the entire
# file's worth of data every time -- fine for small files like this one,
# but something to be aware of for large files.



# ***** Update in the middle of the file *****

# Learned that seek(0) plus writelines() is how you rewrite a file
# after inserting a line, since there's no direct "insert" on disk.
# The same "read everything, modify it in memory as a normal Python
# list, then rewrite the whole file" strategy as above, but manipulating
# a LIST of lines instead of one big string, since inserting into a list
# at a specific position is easy and familiar.
with open("newfile.txt", "r+", encoding="utf-8") as file:
    # readlines() returns every line of the file as a separate string in
    # a list (see reading.py in this folder for more on readlines()).
    lines = file.readlines()
    # list.insert(index, value) shifts every existing element at and
    # after `index` one position later, then places `value` at that
    # index. Inserting at index 1 puts "Yilmaz Aygun\n" right after
    # whatever was originally the first line, becoming the new second
    # line, and pushing everything that used to come after it down by
    # one position.
    lines.insert(1, "Yilmaz Aygun\n")
    # Move the cursor back to the very start before writing, otherwise
    # writelines() would start writing from wherever readlines() left
    # the cursor (the end of the file), which isn't what we want here.
    file.seek(0)
    # file.writelines(list_of_strings) writes each string in the list
    # out one after another, with NO automatic newlines added between
    # them (unlike print()) -- which is exactly why each string in
    # `lines` already carries its own trailing "\n" from readlines().
    # Note this does not erase anything on its own; since the new
    # content here happens to be at least as long as what was there
    # before, it simply overwrites the old content correctly, but this
    # approach can leave leftover old characters at the end of the file
    # if the new content were ever shorter than the old.
    file.writelines(lines)

# Re-opening (in plain "r" mode this time) just to read back and print
# the final result, confirming the new line landed in the right place.
with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
