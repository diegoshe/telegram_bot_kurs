from models import Bank

from bs4 import BeautifulSoup
import requests


def parse_website():
    URL = 'https://ftime.by/kursy-valyut/minsk'
    res = requests.get(URL).content
    soup = BeautifulSoup(res, "html.parser")

    for d in soup.find_all('tbody'):
        for c in d.find_all('tr'):
            try:
                bank = c.find('a').string
                bank_buys = c.find('div', 'field-kurs-pokupka-usd').string[5:9]
                bank_selling = c.find('div', 'field-kurs-sale-usd').string[5:9]
            except:
                continue
            Bank.create(name=bank, buy=bank_buys, sells=bank_selling)


def main():
    parse_website()


if __name__ == '__main__':
    main()