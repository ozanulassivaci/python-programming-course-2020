# First time hitting a real public API and using its response to do a calculation.
import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

from_currency = input("currency to convert from: ")
to_currency = input("currency to convert to: ")
amount = int(input(f"How much {from_currency} do you want to convert: "))

result = requests.get(api_url+from_currency)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(from_currency, result["rates"][to_currency], to_currency))
print("{0} {1} = {2} {3}".format(amount, from_currency, amount * result["rates"][to_currency],to_currency))

