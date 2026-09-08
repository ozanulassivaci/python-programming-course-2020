# Poking around the os module - mostly commented out so I don't accidentally
# create/rename/delete real folders while testing.
#
# The os module is Python's interface to the operating system: creating,
# renaming and deleting files/folders, inspecting the filesystem, reading
# environment info, and building file paths in a way that works on Windows,
# macOS and Linux alike.
import os
import datetime

# dir(os) lists every name (function, constant, ...) defined inside the os
# module - a quick way to see what's available without opening documentation.
result = dir(os)
# os.name reports which family of OS you're running on: 'nt' on Windows,
# 'posix' on Linux/macOS.
result = os.name

# changing directory
# os.chdir(path) changes the current working directory for the running
# program - similar to typing "cd" in a terminal.
# os.chdir('C:\\')
# os.chdir('../..')

# creating a folder
# os.mkdir(path) creates a single new folder (fails if a parent folder in
# the path doesn't already exist).
# os.mkdir("newdirectory")
# os.makedirs(path) creates a folder AND any missing parent folders needed
# to reach it, all in one call.
# os.makedirs("newdirectory/new_folder")
# os.rename(old, new) renames a file or folder.
# os.rename("newdirectory","new_folder")
# os.rmdir(path) deletes a single, empty folder.
# os.rmdir("newdirectory")
# os.removedirs(path) deletes a folder AND its now-empty parent folders,
# walking upward - the reverse of makedirs().
# os.removedirs("new_folder/new_folder")

# listing
# os.listdir() returns a list of the names of every file/folder directly
# inside the given path (or inside the current working directory if no
# path is given).
# result = os.listdir()
# result = os.listdir('C:\\')
# for filename in os.listdir():
#     if filename.endswith('.py'):
#         print(filename)


# getting the current working directory
# os.getcwd() ("get current working directory") returns the folder the
# script is currently running from, as a string path.
# result = os.getcwd()


# os.stat(path) returns a stat_result object with low-level filesystem
# metadata about a file: its size, and three timestamps (as raw numbers of
# seconds since the epoch - see _datetime.py for what that means).
# result = os.stat("_datetime.py")
# result = result.st_size/1024  # size in KB instead of bytes
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # creation date
# result = datetime.datetime.fromtimestamp(result.st_atime)  # last access date
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # last modified date

# os.system(command) runs a command in the operating system's shell, exactly
# as if you'd typed it into a terminal - here, it would open Notepad.
# os.system("notepad.exe")

# path
# The os.path sub-module deals specifically with manipulating file PATHS as
# strings/objects, without necessarily touching the actual filesystem.

# os.path.abspath(path) turns a relative path into a full, absolute path by
# prefixing it with the current working directory.
result = os.path.abspath("_os.py")
# os.path.dirname(path) returns everything except the final file/folder name
# - i.e. the containing directory.
result = os.path.dirname("C:/python/advanced-modules/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
# os.path.exists(path) returns True/False depending on whether something
# (file or folder) actually exists at that path right now.
result = os.path.exists("C:/python/advanced-modules/_os1.py")
result = os.path.exists("C:/python/advanced-modules")
# os.path.isdir(path) / os.path.isfile(path) check specifically whether the
# path points to a folder or to a file, respectively.
result = os.path.isdir("C:/python/advanced-modules")
result = os.path.isfile("C:/python/advanced-modules/_os.py")
# os.path.join(*parts) glues path pieces together using the correct
# separator for the current OS (backslash on Windows, forward slash on
# Linux/macOS) - safer than concatenating strings with "+" by hand.
result = os.path.join("C:\\","deneme","deneme1")
# os.path.split(path) splits a path into a (directory, filename) tuple at
# the last separator.
result = os.path.split("C:\\deneme")
# os.path.splitext(path) splits a path into a (name, extension) tuple at
# the last dot, e.g. ("_os", ".py").
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]  # -> ".py", the extension half of the tuple above

print(result)
