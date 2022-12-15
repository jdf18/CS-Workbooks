# Currency converter problem:
from json import loads
from functools import lru_cache

with open('13 Currency Codes.json', 'r') as file:
  CURRENCY_CODE_LUT = loads(file.read())

CODE_CURRENCY_LUT = {j: i for i, j in CURRENCY_CODE_LUT.items()}


@lru_cache(100)

def get_rates(start_currency):
  import requests
  url = "https://open.er-api.com/v6/latest/%s" % (start_currency)

  response = requests.get(url)
  data = response.json()["rates"]
  return data


RATES = get_rates("GBP")


def convert_currency(amount, end_currency):
  print("%s %s = %s %s" %
        (amount, CODE_CURRENCY_LUT['GBP'],
         (amount * RATES[end_currency]), CODE_CURRENCY_LUT[end_currency]))
  return amount * RATES[end_currency]


convert_currency(float(input('Amount: ')), input("Currency code: "))
