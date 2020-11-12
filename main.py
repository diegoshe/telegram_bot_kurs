from models import Bank, User

import datetime


def creat_user_bd(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_name = message.from_user.username
    try:
        User.get(User.userId == user_id)
    except User.DoesNotExist:
        User.create(userId=user_id, first_name=first_name, last_name=last_name, user_name=user_name)


def get_data_db():
    data = [{'name': bank.name, 'buy': bank.buy, 'sell': bank.sells} for bank in Bank.select()]
    return data


def format_data_str(data, method):
    format_str = ''
    for d in data:
        name_bank = d['name']
        sel = d['sell']
        buy = d['buy']
        if method == 'Выгодно продать':
            result = f'<b>{name_bank}</b>\nпродает покупает\n <ins><pre>{sel}\t </pre>  <b><em>{buy}</em></b></ins>\n'
        elif method == 'Выгодно купить':
            result = f'<b>{name_bank}</b>\nпродает покупает\n <ins><em><b>{sel}</b></em>  <pre>\t\t {buy}</pre></ins>\n'
        else:
            result = f'<b>{name_bank}</b>\nпродает\t покупает\n <pre>{sel}\t   {buy}</pre>\n'
        format_str += result
    return format_str


def format_data_list(method):
    data = get_data_db()
    format_data = []
    for d in data:
        name_bank = d['name']
        sel = d['sell']
        buy = d['buy']
        result = {
            'name': name_bank,
            'sell': sel,
            'buy': buy
        }
        format_data.append(result)
    if method == 'Выгодно продать':
        sort_data = sorted(format_data, key=lambda x: x['buy'], reverse=True)[:5]
    elif method == 'Выгодно купить':
        sort_data = sorted(format_data, key=lambda x: x['sell'])[:5]
    elif method == 'Курс всех банков':
        sort_data = format_data
    return sort_data


def main():
    print(get_data_db())


if __name__ == '__main__':
    main()
