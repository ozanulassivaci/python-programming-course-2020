# The open() function is used to open and create files.
# Usage: open(file_name, file_mode)
# file_mode => specifies what we're opening the file for.
# open() returns a "file object" that you then read from or write to.
# When you're done, it's important to close the file with .close() (or,
# better, use the "with" statement shown in the other files in this
# folder, which closes it for you automatically) -- an unclosed file can
# keep data buffered in memory instead of actually saved to disk, and
# can keep the file locked against other programs.

# "w": (Write) write mode.
#    ** Creates the file at that location.
#    ** Clears the file content and writes fresh.
# In other words, "w" mode is DESTRUCTIVE: if the file already has
# content, opening it with "w" immediately erases that content (even
# before you write anything new), and if the file doesn't exist yet,
# Python creates a brand-new empty one.

# file = open("newfile.txt","w")
# file = open("C:/users/ozanulassivaci/desktop/newfile.txt","w")
# You can use a relative path (just a filename, resolved relative to
# wherever the script is run from) or a full absolute path like the
# second example here.
# file.close()
# Always matches every open() with a close() (or a "with" block) so the
# operating system knows you're finished with the file.

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Ozan Ulas Sivaci")
# file.close()
# The `encoding` argument tells Python how to translate the text you
# write into raw bytes on disk (and back again when reading). 'utf-8' is
# a very common, safe default that can represent virtually any character
# from any language -- without specifying it, Python would fall back to
# a platform-dependent default encoding, which can cause subtle bugs
# with non-English characters (like Turkish ş, ç, ğ, ü, ö, ı).

# "a": (Append) appending. Creates the file if it doesn't exist at that location.
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nKerem Deniz")
# file.write("Kerem Deniz\n")
# file.close()
# Unlike "w", "a" mode does NOT erase existing content -- new writes are
# added onto the END of whatever is already there. "\n" is the newline
# escape character, which starts a new line; notice the two example
# write() calls put the newline in different places (before vs. after
# the text), which changes where the line break ends up relative to the
# next thing written.

# "x": (Create) creation. Raises an error if the file already exists.
# file = open("newfile2.txt","x",encoding='utf-8')
# "x" mode is for when you specifically want to make sure you're
# creating a brand-new file and NOT accidentally overwriting one that
# already exists -- if "newfile2.txt" already existed, this line would
# raise a FileExistsError instead of silently wiping it like "w" would.

# "r": (Read) reading. default mode. raises an error if the file doesn't exist at that location.
# "r" mode opens an existing file for reading only; you can't write to
# it in this mode. If the file doesn't exist, Python raises a
# FileNotFoundError. This is the default mode used when you don't pass a
# mode argument to open() at all.

# Learned that "w" mode wipes the file first, while "a" mode just appends to it.
