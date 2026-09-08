# First time hitting a real public API and using its response to do a calculation.
#
# An "API" (Application Programming Interface) here means a web address that,
# instead of returning an HTML page for humans to read, returns raw data
# (usually as JSON) meant to be consumed by a program. This script asks a
# currency-exchange-rate API for the latest rates and uses them to convert
# an amount from one currency to another.
import requests
import json

# NOTE: this specific API endpoint may no longer be reachable, may require
# an API key now, or may have changed its response format since this script
# was written - free public APIs change or shut down over time. If this
# script stops working, that's the first thing to check, not a bug in the
# Python code itself.
api_url = "https://api.exchangeratesapi.io/latest?base="

from_currency = input("currency to convert from: ")
to_currency = input("currency to convert to: ")
amount = int(input(f"How much {from_currency} do you want to convert: "))

# requests.get(url) performs an HTTP GET request - the same kind of request
# your browser makes when you visit a web address - and returns a Response
# object once the server replies. Appending from_currency to the URL fills
# in the "base=" query parameter, e.g. base=USD, telling the API "give me
# rates relative to 1 unit of this currency".
result = requests.get(api_url+from_currency)

# result.text is the raw response body as a plain string (here, a JSON
# document). json.loads(...) parses that JSON string into a native Python
# dict, so we can access its fields with square brackets like any other dict.
result = json.loads(result.text)

# The API's JSON response is expected to look roughly like:
#   {"base": "USD", "date": "...", "rates": {"EUR": 0.91, "GBP": 0.78, ...}}
# so result["rates"][to_currency] looks up how many units of to_currency
# equal 1 unit of from_currency.
print("1 {0} = {1} {2}".format(from_currency, result["rates"][to_currency], to_currency))
# .format(0, 1, 2, ...) fills the {0}, {1}, {2} placeholders in order with
# the arguments passed to it - an older alternative to f-strings.
print("{0} {1} = {2} {3}".format(amount, from_currency, amount * result["rates"][to_currency],to_currency))
