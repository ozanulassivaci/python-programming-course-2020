# requests + json together: fetch some data, then filter it in plain Python.
#
# The requests library is the standard way to make HTTP calls from Python
# (fetching web pages or talking to APIs) - much friendlier than Python's
# built-in urllib. Here we call a free "fake" REST API (jsonplaceholder)
# that returns sample to-do items as JSON, purely for practicing the
# request -> parse -> filter workflow.
import requests
import json

# requests.get(url) sends an HTTP GET request (the kind used to "fetch" a
# resource, as opposed to POST, which "sends" data) and returns a Response
# object once the server answers. Note: this depends on jsonplaceholder.typicode.com
# being reachable and returning the same shape of data - like any external
# service, it could change or go offline in the future.
result = requests.get("https://jsonplaceholder.typicode.com/todos")

# result.text is the raw response body as a string. json.loads(...) parses
# that JSON text into native Python data - here, a list of dicts, since the
# API returns a JSON array of to-do objects like:
#   {"userId": 1, "id": 1, "title": "...", "completed": false}
result = json.loads(result.text)

# Loop through every to-do item and only print the title of the ones that
# belong to userId 1 - i.e. filtering the data in plain Python after
# fetching all of it (rather than asking the API to filter server-side).
for i in result:
    if i["userId"] == 1:
        print(i["title"])

print(type(result))  # <class 'list'> - confirms json.loads() gave us a Python list here
