# Notes on converting between a JSON string and a Python dict, both ways.
#
# JSON (JavaScript Object Notation) is a text format for structured data
# that looks a lot like Python dict/list literals, and is the most common
# format used to exchange data between programs over the web (APIs, config
# files, etc). Python's json module converts between JSON text and native
# Python objects (dict, list, str, int, float, bool, None).
import json

# A JSON string: valid JSON requires double quotes around keys/string
# values (single quotes are not allowed in real JSON), which is why this is
# written as a Python string containing double quotes.
person_string = '{"name":"Ali", "languages":["python","C#"]}'
# The equivalent already-parsed data, written directly as a Python dict.
person_dict = {"name": "Ali","languages": ["Python","C#"] }

# JSON string to Dict
# json.loads(json_string) ("load string") parses a JSON-formatted string
# and returns the equivalent Python object - here, a dict with a "languages"
# list nested inside it.
# result = json.loads(person_string)
# result = result["name"]        # -> "Ali"
# result = result["languages"]   # -> ["python", "C#"]

# json.load(file_object) ("load", no "s") does the same parsing, but reads
# the JSON text directly from an already-open file instead of from a string
# you already have in memory.
# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])


# Dict to JSON string
# json.dumps(python_object) ("dump string") does the reverse: it converts a
# Python object into a JSON-formatted string.
# result = json.dumps(person_dict)
# print(type(result))  # <class 'str'> - proof that dumps() returns text, not a dict

# json.dump(python_object, file_object) ("dump", no "s") writes the JSON
# text directly into an already-open file instead of returning it as a string.
# with open("person.json","w") as f:
#     json.dump(person_dict, f)

# person_dict = json.loads(person_string)

# dumps() accepts extra formatting options:
#   indent=4    -> pretty-print with 4 spaces of indentation per nesting level
#                  (otherwise everything is squeezed onto a single line)
#   sort_keys=True -> alphabetically sort the dict's keys in the output,
#                      regardless of the order they were inserted in
# result = json.dumps(person_dict, indent= 4, sort_keys= True)
# print(person_dict)
# print(result)
