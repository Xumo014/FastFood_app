from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

def get_product_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f'SELECT * FROM food_product WHERE id=%s', [product_id])
        product = dictfetchone(cursor)
        return product

def get_orderproduct_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f'SELECT * FROM food_orderproduct WHERE id=%s', [product_id])
        product = dictfetchone(cursor)
        return product

def get_user_by_phone(phone):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f'SELECT * FROM food_customer WHERE phone=%s', [phone])
        user = dictfetchone(cursor)
        return user


