""" Test class for the house and condo class """
import unittest
from house import House
from house import Condo


class HouseTest(unittest.TestCase):
    def setUp(self):
        self.my_house = House('Concrete', 'Shingle', 'Red', 45)
        self.my_condo = Condo('Bricks', 'Steel', 'Yellow', 50, 'Wrap Around')

    def test_house_found(self):
        self.assertIs(self.my_house.foundation, 'Concrete')

    def test_house_found_set(self):
        self.my_house.foundation = 'Cement'
        self.assertEqual(self.my_house.foundation, 'Cement')

    def test_condo_found(self):
        self.assertIs(self.my_condo.foundation, 'Bricks')

    def test_house_window(self):
        self.assertIs(self.my_house.window_size, 45)


if __name__ == '__main__':
    unittest.main()
