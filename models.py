from peewee import *
import datetime


db = SqliteDatabase('banks.db')

#unique=True
class Bank(Model):
    name = CharField()
    buy = CharField(null=True)
    sells = CharField(null=True)
    date = DateTimeField(default=datetime.datetime.now().strftime("%d-%m-%Y"))

    class Meta:
        database = db
        table_name = 'bank'


class Branch(Model):
    bank = ForeignKeyField(Bank, backref='branches')
    adress = CharField(null=True)
    phone_number = CharField(null=True)

    class Meta:
        database = db


class User(Model):
    userId = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    user_name = CharField(null=True)
    date = DateTimeField(default=datetime.datetime.now().strftime("%d-%m-%Y"))

    class Meta:
        database = db


def init_db():
    db.drop_tables([Bank, Branch, User], safe=True)
    db.create_tables([Bank, Branch, User], safe=True)


if __name__ == '__main__':
    init_db()