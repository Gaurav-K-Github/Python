from currency_converter import CurrencyConverter
c = CurrencyConverter()
amount = 100
from_currency = 'USD'
to_currency = 'EUR'
converted_amount = c.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
