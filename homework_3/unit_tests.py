import unittest
from homework_3.test_simple_calc import *
from homework_3.tests_simple_employee import *
from unittest import mock

class TestCalc(unittest.TestCase):
    # multiply() block
    def test_str_multiply(self):
        # test string case
        with self.assertRaises(TypeError):
            multiply('22', '22')
        self.assertEqual(multiply('22', 4), '22'*4)

    def test_number_multiply_one(self):
        # test number case
        # multiply 1 on number
        self.assertEqual(multiply(1, 1), 1)

        self.assertEqual(multiply(1, 0.5), 0.5)
        self.assertEqual(multiply(1, 2), 2)

        self.assertEqual(multiply(0.5, 1), 0.5)
        self.assertEqual(multiply(2, 1), 2)

        self.assertNotEqual(multiply(2, 1), 3)


    def test_number_multiply_float(self):
        # test number case
        # multiply int on float
        self.assertEqual(multiply(2, 0.5), 1)
        self.assertEqual(multiply(0.5, 2), 1)

        self.assertNotEqual(multiply(0.5, 2), 2)


    def test_number_multiply_neg_int(self):
        # test number case
        # multiply int on negative int
        self.assertEqual(multiply(2, -1), -2)
        self.assertEqual(multiply(0.5, -2), -1)

        self.assertNotEqual(multiply(0.5, -2), 0)


    def test_number_multiply_complex(self):
        # test number case
        # multiply complex on complex
        self.assertEqual(multiply(complex(0, 1), complex(0, 1)), -1)


    def test_number_multiply_zero(self):
        # test number case
        # multiply 0 on number
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

        self.assertNotEqual(multiply(0, 0), 1)



    # division() block
    def test_zero_division(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
        with self.assertRaises(ValueError):
            divide(1, 0.1**999)

    def test_str_division(self):
        with self.assertRaises(TypeError):
            divide('1', '2')
        with self.assertRaises(TypeError):
            divide('1', 2)
        with self.assertRaises(TypeError):
            divide(2, '1')

    def test_number_division(self):
        # divide number by 1
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(divide(2, 1), 2)
        self.assertEqual(divide(0.5, 1), 0.5)

        # divide 5 by 5
        self.assertEqual(divide(5, 5), 1)

        # divide 0 by number
        self.assertEqual(divide(0, 5), 0)

        # divide number by float
        self.assertEqual(divide(2, 0.5), 4)


    # add() block
    def test_str_add(self):
        # errors handle
        with self.assertRaises(TypeError):
            add('1', 2)
        with self.assertRaises(TypeError):
            add(2, '1')
        # concatenate strings
        self.assertEqual(add('1', '2'), '12')

    def test_number_add(self):
        # add number to 1
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(0.5, 1), 1.5)

        # add 5 to 5
        self.assertEqual(add(5, 5), 10)

        # add -5 to 5
        self.assertEqual(add(-5, 5), 0)



    # subtract() block
    def test_str_subtract(self):
        # errors handle
        with self.assertRaises(TypeError):
            subtract('1', 2)
        with self.assertRaises(TypeError):
            subtract(2, '1')
        with self.assertRaises(TypeError):
            subtract('1', '2')

    def test_number_subtract(self):
        # subtract number on 1
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(0.5, 1), -0.5)

        # subtract 5 on 5
        self.assertEqual(subtract(5, 5), 0)

        # subtract 5 to -5
        self.assertEqual(subtract(5, -5), 10)


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee('1', '2', 3)
        self.employee_int = Employee(1, 2, 3)
        self.employee_str = Employee('1', '2', '12')

    def test_email(self):
        self.assertEqual(self.employee.email, '1.2@email.com')
        self.assertEqual(self.employee_int.email, '1.2@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, '1 2')
        self.assertEqual(self.employee_int.fullname, '1 2')

    def test_apply_raise(self):
        test_e = Employee('1', '2', 1)
        pr_pay = test_e.pay
        test_e.apply_raise()

        self.assertEqual(test_e.pay, int(pr_pay*1.05))

        with self.assertRaises(TypeError):
            test_e = Employee('1', '2', '12')
            self.employee_str.apply_raise()

    def mock_request(self):
        class Requests:
            def get(self, text):
                pass
            ok = True
        return Requests()

    @mock.patch('homework_3.tests_simple_employee.requests',
                side_effect=mock_request)
    def test_monthly_schedule(self, response):
        self.employee.monthly_schedule(11)


if __name__ == '__main__':
    unittest.main(verbosity=2)
