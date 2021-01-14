import unittest
from unittest.mock import patch

from homework.tests_simple_employee import *


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.person = Employee('Harry', 'Potter', 100)

    def tearDown(self):
        del self.person

    def test_email(self):
        self.assertEqual(self.person.email, 'Harry.Potter@email.com')

    def test_fullname(self):
        self.assertEqual(self.person.fullname, 'Harry Potter')

    def test_apply_raise(self):
        self.person.apply_raise()
        self.assertEqual(self.person.pay, 105)

    def test_monthly_schedule(self):
        with patch('tests_simple_employee.requests.get') as mock:
            mock.return_value.ok = False
            mock.return_value.text = 'Done'

            schedule = self.person.monthly_schedule('01')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
