# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("test")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

# ***** Update at the end of the file *****

# with open("newfile.txt","a", encoding="utf-8") as file:
#     file.write("\nOznur")

# ***** Update at the start of the file *****

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Aykut\n" + content
#     file.seek(0)
#     file.write(content)



# ***** Update in the middle of the file *****

# Learned that seek(0) plus writelines() is how you rewrite a file
# after inserting a line, since there's no direct "insert" on disk.
with open("newfile.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    lines.insert(1, "Yilmaz Aygun\n")
    file.seek(0)
    file.writelines(lines)

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
