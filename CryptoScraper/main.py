from crypto_scraper import CryptoCurrency
import time
import os

# We have used the most "HOT" cryptos for reference.
if __name__ == '__main__':
    while True:
        symbol1 = CryptoCurrency(symbol='BTCUSD')
        symbol2 = CryptoCurrency(symbol='ETHUSD')
        symbol3 = CryptoCurrency(symbol='BNBUSDT')
        symbol4 = CryptoCurrency(symbol='DOGEUSDT')
        symbol5 = CryptoCurrency(symbol='BTCSTUSDT')
        symbol6 = CryptoCurrency(symbol='SXPUSDT')
        symbol7 = CryptoCurrency(symbol='SHIBUSDT')
        symbol8 = CryptoCurrency(symbol='SOLUSDT')
        symbol9 = CryptoCurrency(symbol='MATICUSDT')
        symbol10 = CryptoCurrency(symbol='TRXUSDT')

        CryptoCurrency.show_prices()
        time.sleep(1)
        CryptoCurrency.clean_prices()
        os.system("cls")

# Create more objects of CryptoCurrency here if you'd like to add to the table of contents
# symbol{x} = CryptoCurrency(symbol='xrpusdt')
