# Learned that seek(0) resets the cursor back to the start of the file.
with open("newfile.txt", "r", encoding="utf-8") as file:
    content = file.read(10)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)
