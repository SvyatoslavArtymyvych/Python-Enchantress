import unittest
from unittest.mock import patch
from hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        self.hen_house = HenHouse(15)

    def test_init_with_less_than_min(self):
        with self.assertRaises(ValueError) as e:
            self.hen_house = HenHouse(3)

    def test_season(self):
        with patch('hen_class.datetime.datetime') as e:
            e.today().month = 1
            self.assertEqual(self.hen_house.season, 'winter')

            e.today().month = 9
            self.assertEqual(self.hen_house.season, 'autumn')

    def test_productivity_index(self):
        with patch('hen_class.datetime.datetime') as e:
            e.today().month = 1
            self.hen_house.season
            print(self.hen_house.season)
            self.assertEqual(self.hen_house._productivity_index(),
                             self.hen_house.hens_productivity['winter'])

    def test_productivity_index_incorrect_season(self):
        with patch('hen_class.datetime.datetime') as e:
            e.today().month = -1
            self.hen_house.season

            with self.assertRaises(ErrorTimesOfYear):
                self.hen_house._productivity_index()

    @patch('hen_class.HenHouse._productivity_index', return_value=0.25)
    def test_get_eggs_daily_in_winter(self, productivity_index):
        self.assertEqual(self.hen_house.get_eggs_daily(self.hen_house.hen_count), 3)

    @patch('hen_class.HenHouse._productivity_index', return_value=0.25)
    def test_get_max_count_for_soup(self, productivity_index):
        self.assertEqual(self.hen_house.get_max_count_for_soup(1), 8)

    @patch('hen_class.HenHouse._productivity_index', return_value=0.25)
    def test_get_max_count_for_soup_returns_zero(self, productivity_index):
        self.assertEqual(
            self.hen_house.get_max_count_for_soup(self.hen_house.get_eggs_daily(self.hen_house.hen_count+10)), 0)

    def test_food_price(self):
        with patch('hen_class.requests.get') as e:
            e.return_value.status_code = 200
            e.return_value.page_text = '12345678901234567890'

            self.assertIsInstance(self.hen_house.food_price(), int)

    def test_food_price_connection_error(self):
        with patch('hen_class.requests.get') as e:
            e.return_value.status_code = 404

            with self.assertRaises(ConnectionError):
                self.hen_house.food_price()


if __name__ == '__main__':
    unittest.main()