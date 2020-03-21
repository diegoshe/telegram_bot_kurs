from urllib.request import urlopen
from bs4 import BeautifulSoup


def parse_website():
    res = urlopen('https://ftime.by/kursy-valyut/minsk').read()
    soup = BeautifulSoup(res, "html.parser")

    data = []
    for d in soup.find_all('tbody'):
        for c in d.find_all('tr'):
            try:
                bank = c.find('a').string
                bank_buys = c.find('div', 'field-kurs-pokupka-usd').string[5:9]
                bank_selling = c.find('div', 'field-kurs-sale-usd').string[5:9]
            except:
                continue
            info = {
                'bank': bank,
                'bank_selling': bank_selling,
                'bank_buys': bank_buys
            }
            data.append(info)

    return data


def format_data_str(data, method):
    format_str = ''
    for d in data:
        print('***d', d)
        name_bank = d['bank']
        sel = d['bank_selling']
        buy = d['bank_buys']
        if method == 'Выгодно продать':
            result = f'<b>{name_bank}</b>\nпродает покупает\n <ins><em>{sel}</em><pre>\t\t\t</pre><b>{buy}</b></ins>\n'
        elif method == 'Выгодно купить':
            result = f'<b>{name_bank}</b>\nпродает покупает\n <ins><em><b>{sel}</b></em><pre>\t\t\t{buy}</pre></ins>\n'
        else:
            result = f'<b>{name_bank}</b>\nпродает покупает\n <ins><em>{sel}</em><pre>\t\t\t{buy}</pre></ins>\n'
        format_str += result
    return format_str


def format_data_list(data, method):
    format_data = []
    for d in data:
        name_bank = d['bank']
        sel = d['bank_selling']
        buy = d['bank_buys']
        result = {
            'bank': name_bank,
            'bank_selling': sel,
            'bank_buys': buy
        }
        format_data.append(result)
    if method == 'Выгодно продать':
        sort_data = sorted(format_data, key=lambda x: x['bank_buys'], reverse = True)[:5]
        print('Выгодно продать')
    else:
        sort_data = sorted(format_data, key=lambda x: x['bank_selling'])[:5]
        print('Выгодно купить')
    return sort_data


data = parse_website()
print('***data!!!')
def get_data_sort(method):
    format_list = format_data_list(data, method)
    return format_list
