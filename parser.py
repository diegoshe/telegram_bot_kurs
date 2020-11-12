from models import Bank

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def parse_website():
    site = 'https://ftime.by/kursy-valyut/minsk'

    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    for d in soup.find_all('tbody'):
        for c in d.find_all('tr'):
            try:
                bank = c.find('a').string
                bank_buys = c.find('div', 'field-kurs-pokupka-usd').string[5:9]
                bank_selling = c.find('div', 'field-kurs-sale-usd').string[5:9]
            except Exception as e:
                print('***ERROR parser.py - ', e)
                continue
            Bank.create(name=bank, buy=bank_buys, sells=bank_selling)


def main():
    parse_website()


if __name__ == '__main__':
    main()
