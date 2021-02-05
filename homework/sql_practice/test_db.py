import unittest
from unittest import TestCase
import datetime

from db import DatabaseClass


class TestPositiveDatabaseCRUD(TestCase):
    def setUp(self) -> None:
        self.db = DatabaseClass()
        self.user = {'name': 'Ivan', 'email': 'ivan@gmail.com', 'registration_time': '2021-02-05 15:31:26'}

    def test_crud_user(self):
        new_info = {'name': 'Ivanko', 'email': 'ivan_new@gmail.com', 'registration_time': '2021-03-05 15:31:26'}
        self.user_id = self.db.get_last_user_id()

        self.db.create_user(self.user)
        self.user_id = self.db.get_last_user_id()
        self.assertEqual(self.db.read_user_info(self.user_id),
                         ('Ivan', 'ivan@gmail.com', datetime.datetime(2021, 2, 5, 15, 31, 26)))

        self.db.update_user(new_info, self.user_id)
        self.assertEqual(self.db.read_user_info(self.user_id),
                         ('Ivanko', 'ivan_new@gmail.com', datetime.datetime(2021, 3, 5, 15, 31, 26)))

        self.db.delete_user(self.user_id)
        self.assertEqual(self.db.read_user_info(self.user_id), None)

    def test_crud_cart(self):
        self.db.create_user(self.user)
        self.user_id = self.db.get_last_user_id()
        self.cart_id = self.db.get_last_cart_id()

        self.cart = {'creation_time': '2021-03-05 15:31:26',
                     'user_id': self.user_id,
                     'cart_details': [
                         {'product': 'Orange', 'price': '1', },
                         {'product': 'Apple', 'price': '2'},
                         {'product': 'Pear', 'price': '3'}
                     ]
                     }
        self.cart_new = {'creation_time': '2021-03-05 20:00:00',
                         'user_id': self.user_id,
                         'cart_details': [
                             {'product': 'Pineapple', 'price': '1'},
                             {'product': 'Mandarin', 'price': '2'}
                         ]
                         }

        self.db.create_cart(self.cart)

        self.assertEqual(self.db.read_cart(self.db.get_last_cart_id()),
                         [(5, 'Orange', 1), (5, 'Apple', 2), (5, 'Pear', 3)])

        self.db.update_cart(self.cart_new)

        self.assertEqual(self.db.read_cart(self.db.get_last_cart_id()),
                         [(5, 'Pineapple', 1), (5, 'Mandarin', 2)])

        self.db.delete_cart(self.db.get_last_cart_id())

        self.assertEqual(self.db.read_cart(self.db.get_last_cart_id() + 1), [])

        self.db.delete_user(self.user_id)


class TestNegativeDatabaseCRUD(TestCase):
    def setUp(self) -> None:
        self.db = DatabaseClass()
        self.user = {'name': 'Igor', 'email': 'igor@gmail.com', 'registration_time': '2021-02-05 15:31:26'}

    def test_crud_user(self):
        new_info = {'name': 'Igorko', 'email': 'igor_new@gmail.com', 'registration_time': '2021-03-05 15:31:26'}
        self.user_id = self.db.get_last_user_id()

        self.db.create_user(self.user)
        self.user_id = self.db.get_last_user_id()
        self.assertNotEqual(self.db.read_user_info(self.user_id),
                            ('Illia', 'illia@gmail.com', datetime.datetime(2021, 2, 5, 15, 31, 26)))

        self.db.update_user(new_info, self.user_id)
        self.assertNotEqual(self.db.read_user_info(self.user_id),
                            ('Illia', 'illia@gmail.com', datetime.datetime(2021, 3, 5, 15, 31, 26)))

        self.db.delete_user(self.user_id)
        self.assertNotEqual(self.db.read_user_info(self.user_id),
                            ('Igorko', 'igor_new@gmail.com', datetime.datetime(2021, 2, 5, 15, 31, 26)))

    def test_crud_cart(self):
        self.db.create_user(self.user)
        self.user_id = self.db.get_last_user_id()
        self.cart_id = self.db.get_last_cart_id()

        self.cart = {'creation_time': '2021-03-05 15:31:26',
                     'user_id': self.user_id,
                     'cart_details': [
                         {'product': 'Orange', 'price': '1', },
                         {'product': 'Apple', 'price': '2'},
                         {'product': 'Pear', 'price': '3'}
                     ]
                     }
        self.cart_new = {'creation_time': '2021-03-05 20:00:00',
                         'user_id': self.user_id,
                         'cart_details': [
                             {'product': 'Pineapple', 'price': '1'},
                             {'product': 'Mandarin', 'price': '2'}
                         ]
                         }

        self.db.create_cart(self.cart)

        self.assertNotEqual(self.db.read_cart(self.db.get_last_cart_id()),
                            [(5, 'Banana', 1), (5, 'Orange', 2), (5, 'Melon', 3)])

        self.db.update_cart(self.cart_new)

        self.assertNotEqual(self.db.read_cart(self.db.get_last_cart_id()),
                            [(5, 'Potato', 1), (5, 'Carrot', 2)])

        self.db.delete_cart(self.db.get_last_cart_id())

        self.assertNotEqual(self.db.read_cart(self.db.get_last_cart_id() + 1), [(5, 'Potato', 1), (5, 'Carrot', 2)])

        self.db.delete_user(self.user_id)
