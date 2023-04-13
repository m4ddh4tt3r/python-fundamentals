""" Lesson 15 - testing your code """
import unittest
from lesson2 import demo_function3
from lesson12more import Car
""" when you write test cases, you typically focus on specific
 classes or groups of related functions per file. """


class Something(unittest.TestCase):
    def setUp(self):
        self.my_car = Car('Silverado', 'Blue')

    def test_model(self):
        self.assertEqual(self.my_car._model, 'Silverado')

    def test_color(self):
        self.assertEqual(self.my_car._color, 'Blue')

    def test_info(self):
        self.assertIsNone(self.my_car.info())

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_addition(self):
        self.assertIs(demo_function3(5, 5), 10)

    def test_addition_return(self):
        self.assertIsNotNone(demo_function3(5, 5))


if __name__ == '__main__':
    unittest.main()
