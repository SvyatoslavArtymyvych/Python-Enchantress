import psycopg2
from datetime import datetime


class DatabaseClass:
    def __init__(self):
        self.connection = psycopg2.connect(
            database='postgress',
            user='postgress',
            password='pass',
            host='localhost'
        )
        self.connection.autocommit = True
        self.c = self.connection.cursor()

    def create_user(self, user_info: dict):
        self.c.execute('INSERT INTO users (name, email, registration_time) '
                       'VALUES (%(name)s, %(email)s, %(registration_time)s)', user_info)

    def get_last_user_id(self):
        self.c.execute('SELECT id FROM users ORDER BY id DESC LIMIT 1')
        return int(self.c.fetchone()[0])

    def read_user_info(self, _id: int):
        self.c.execute('SELECT name, email, registration_time FROM users WHERE id = %s' % _id)
        return self.c.fetchone()

    def update_user(self, new_info: dict, _id: int):
        self.c.execute(
            f"UPDATE users SET name = %(name)s, email = %(email)s, registration_time = %(registration_time)s "
            f"WHERE id={_id}", new_info)

    def delete_user(self, _id: int):
        self.c.execute('DELETE FROM users WHERE id = %s' % _id)

    def create_cart(self, cart: dict):
        self.c.execute('INSERT INTO cart (creation_time, user_id) '
                       'VALUES (%(creation_time)s, %(user_id)s)', cart)

        for product in cart['cart_details']:
            self.c.execute(f'INSERT INTO cart_details (cart_id, price, product) '
                           f'VALUES ((SELECT id FROM cart WHERE user_id = {cart["user_id"]} '
                           f'ORDER BY creation_time DESC LIMIT 1), '
                           f'%(price)s, %(product)s)', product)

    def get_last_cart_id(self):
        self.c.execute('SELECT id FROM cart ORDER BY id DESC LIMIT 1')
        return int(self.c.fetchone()[0])

    def read_cart(self, _id: int):
        self.c.execute('SELECT cart_id, product, price FROM cart_details WHERE cart_id = %s' % _id)

        return self.c.fetchall()

    def update_cart(self, cart: dict):
        self.c.execute("UPDATE cart SET creation_time = %(creation_time)s "
                       "WHERE user_id = %(user_id)s", cart)
        # for product in cart['cart_details']:
        #     self.c.execute("UPDATE cart_details SET product = %(product)s, price = %(price)s "
        #                    "WHERE cart_id = %(cart_id)s", product)
        self.c.execute('DELETE FROM cart_details WHERE cart_id = '
                       '(SELECT id FROM cart WHERE user_id = %s)' % cart["user_id"])
        for product in cart['cart_details']:
            self.c.execute(f'INSERT INTO cart_details (cart_id, price, product) '
                           f'VALUES ((SELECT id FROM cart WHERE user_id = {cart["user_id"]} '
                           f'ORDER BY creation_time DESC LIMIT 1), '
                           f'%(price)s, %(product)s)', product)

    def delete_cart(self, _id: int):
        self.c.execute('DELETE FROM cart_details WHERE cart_id = %s' % _id)
        self.c.execute('DELETE FROM cart WHERE id = %s' % _id)
