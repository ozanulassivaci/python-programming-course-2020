# The open() function is used to open and create files.
# Usage: open(file_name, file_mode)
# file_mode => specifies what we're opening the file for.

# "w": (Write) write mode.
#    ** Creates the file at that location.
#    ** Clears the file content and writes fresh.

# file = open("newfile.txt","w")
# file = open("C:/users/ozanulassivaci/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Ozan Ulas Sivaci")
# file.close()

# "a": (Append) appending. Creates the file if it doesn't exist at that location.
# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nKerem Deniz")
# file.write("Kerem Deniz\n")
# file.close()

# "x": (Create) creation. Raises an error if the file already exists.
# file = open("newfile2.txt","x",encoding='utf-8')

# "r": (Read) reading. default mode. raises an error if the file doesn't exist at that location.

# Learned that "w" mode wipes the file first, while "a" mode just appends to it.
