import unittest

from homework.test_simple_calc import *


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_division(self):
        self.assertEqual(divide(6, 2), 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as e:
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
