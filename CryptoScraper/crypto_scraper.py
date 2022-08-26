import requests
import os
from prettytable import PrettyTable

# In order to avoid piracy for API_KEY we have used it as binary for one time, you can refer to README.md for the same.

api_key = os.environ.get("api_key")
class CryptoCurrency:
    base_url = "https://cloud.iexapis.com/stable/crypto"
    prices = []
    def __init__(self, symbol):
        self.symbol = symbol
        self.add_prices_to_list()

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={api_key}"

    @property
    def price(self):
        req = requests.get(self.complete_url).json()
        return float(req.get('price'))

    def add_prices_to_list(self):
        CryptoCurrency.prices.append(
            [self.price, self.symbol])

    @staticmethod
    # Serves the purpose of displaying table contents.
    def prices_table():
        pt = PrettyTable(["Prices", "Crypto Name"])
        pt.add_rows(CryptoCurrency.prices)
        return pt

    @staticmethod
    # Serves the purpose of cleaning the prices in table.
    def clean_prices():
        CryptoCurrency.prices.clear()

    @staticmethod
    # Serves the purpose of displaying the prices in table.
    def show_prices():
        print(CryptoCurrency.prices_table())

