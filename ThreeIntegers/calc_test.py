import unittest

from ThreeIntegers.app import ThreeIntegers


class ThreeIntegersTest(unittest.TestCase):
    def test_integer_product(self):
        Calc = ThreeIntegers([10, 8, 7, 5, 2, 1])

        self.assertEqual(Calc.find(), 10*8*7)

    def test_negative_numbers(self):
        Calc = ThreeIntegers([-10, -10, 1, 3, 2])

        self.assertEqual(Calc.find(), -10*-10*3)

    def test_only_one_negative_number(self):
        Calc = ThreeIntegers([-10, 10, 1, 3, 2])

        self.assertEqual(Calc.find(), 10*3*2)

if __name__ == '__main__':
    unittest.main()
