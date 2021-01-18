import unittest
from unittest.mock import patch, Mock
from hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        # optional method, may be used to initialize hen_house instance
        self.house = HenHouse(6)

    def test_init_with_less_than_min(self):
        # initialize HenHouse with hens_count less than HenHouse.min_hens_accepted
        # make sure error is raised
        with self.assertRaises(ValueError):
            HenHouse(4)

    class MockDatetime:
        def __init__(self, month):
            self.month = month

        def today(self):
            return self

    @patch('hen_class.datetime.datetime', MockDatetime(1))
    def test_season_winter(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        self.assertEqual(self.house.season, 'winter')

    @patch('hen_class.datetime.datetime', MockDatetime(4))
    def test_season_spring(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        self.assertEqual(self.house.season, 'spring')

    @patch('hen_class.datetime.datetime', MockDatetime(7))
    def test_season_summer(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        self.assertEqual(self.house.season, 'summer')

    @patch('hen_class.datetime.datetime', MockDatetime(10))
    def test_season_autumn(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        self.assertEqual(self.house.season, 'autumn')

    @patch('hen_class.HenHouse.season', 'winter')
    def test_productivity_index_winter(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        self.assertEqual(self.house._productivity_index(), 0.25)

    @patch('hen_class.HenHouse.season', 'spring')
    def test_productivity_index_spring(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        self.assertEqual(self.house._productivity_index(), 0.75)


    @patch('hen_class.HenHouse.season', 'summer')
    def test_productivity_index_summer(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        self.assertEqual(self.house._productivity_index(), 1)


    @patch('hen_class.HenHouse.season', 'autumn')
    def test_productivity_index_autumn(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        self.assertEqual(self.house._productivity_index(), 0.5)

    @patch('hen_class.HenHouse.season', 'incorrect')
    def test_productivity_index_incorrect_season(self):
        # mock the season method return with some incorrect season
        # make sure ErrorTimesOfYear is raised when _productivity_index called
        with self.assertRaises(ErrorTimesOfYear):
            self.house._productivity_index()

    @patch('hen_class.HenHouse.season', 'winter')
    def test_get_eggs_daily_in_winter(self):
        # test get_eggs_daily function
        # _productivity_index method or season should be mocked
        self.assertEqual(self.house.get_eggs_daily(self.house.hen_count),
                         int(self.house.hen_count
                         * self.house._productivity_index()))

    @patch('hen_class.HenHouse.season', 'winter')
    def test_get_max_count_for_soup_winter(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        # test eggs count
        expected_eggs = 4
        hen_count = 20
        test_house = HenHouse(hen_count)

        self.assertEqual(
            test_house.get_max_count_for_soup(expected_eggs),
            int((int(hen_count * test_house._productivity_index())
                - expected_eggs)
                / test_house.hens_productivity['winter']
            )
        )

    @patch('hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup_summer(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        # test eggs count
        expected_eggs = 4
        hen_count = 20
        test_house = HenHouse(hen_count)

        self.assertEqual(
                test_house.get_max_count_for_soup(expected_eggs),
                int((int(hen_count * test_house._productivity_index())
                     - expected_eggs)
                    / test_house.hens_productivity['summer']
                    )
                )

    @patch('hen_class.HenHouse.season', 'autumn')
    def test_get_max_count_for_soup_autumn(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        # test eggs count
        expected_eggs = 4
        hen_count = 20
        test_house = HenHouse(hen_count)

        self.assertEqual(
                test_house.get_max_count_for_soup(expected_eggs),
                int((int(hen_count * test_house._productivity_index())
                     - expected_eggs)
                    / test_house.hens_productivity['autumn']
                    )
                )

    @patch('hen_class.HenHouse.season', 'spring')
    def test_get_max_count_for_soup_spring(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        # test eggs count
        expected_eggs = 4
        hen_count = 20
        test_house = HenHouse(hen_count)

        self.assertEqual(
                test_house.get_max_count_for_soup(expected_eggs),
                int((int(hen_count * test_house._productivity_index())
                     - expected_eggs)
                    / test_house.hens_productivity['spring']
                    )
                )

    def test_get_max_count_for_soup_returns_zero(self):
        # call get_max_count_for_soup with expected_eggs number bigger than get_eggs_daily(self.hen_count)
        # zero should be returned.

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        # test if hen_count < min_hens_accepted
        test_house = HenHouse(6)
        test_house.hen_count = 2
        self.assertEqual(test_house.get_max_count_for_soup(1), 0)
        # test if get_eggs_daily(hen_count) < expected_eggs
        self.assertEqual(self.house.get_max_count_for_soup(99), 0)

    class MockRequest():
        def __init__(self, code, text = range(20)):
            self.status_code = code
            self.text = text

        def get(self, text):
            return self

    @patch('hen_class.requests', MockRequest(200))
    def test_food_price(self):
        # mock requests.get and make the result has status_code attr 200 and text to some needed value
        # make sure food-price() return will be of int type
        self.assertEqual(type(self.house.food_price()), int)

    @patch('hen_class.requests', MockRequest(201))
    def test_food_price_connection_error(self):
        # mock requests.get and make the result has status_code attr not 200
        # check that ConnectionError is raised when food_price method called
        with self.assertRaises(ConnectionError):
            self.house.food_price()



if __name__ == '__main__':
    unittest.main(verbosity=2)