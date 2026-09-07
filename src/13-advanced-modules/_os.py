# Poking around the os module - mostly commented out so I don't accidentally
# create/rename/delete real folders while testing.
import os
import datetime

result = dir(os)
result = os.name

# changing directory
# os.chdir('C:\\')
# os.chdir('../..')

# creating a folder
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/new_folder")
# os.rename("newdirectory","new_folder")
# os.rmdir("newdirectory")
# os.removedirs("new_folder/new_folder")

# listing
# result = os.listdir()
# result = os.listdir('C:\\')
# for filename in os.listdir():
#     if filename.endswith('.py'):
#         print(filename)


# getting the current working directory
# result = os.getcwd()


# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # creation date
# result = datetime.datetime.fromtimestamp(result.st_atime)  # last access date
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # last modified date

# os.system("notepad.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/python/advanced-modules/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/python/advanced-modules/_os1.py")
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules")
result = os.path.isfile("C:/python/advanced-modules/_os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)