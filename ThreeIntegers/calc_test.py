import unittest

from ThreeIntegers.app import ThreeIntegers


class ThreeIntegersTest(unittest.TestCase):
    def test_integer_product(self):
        Calc = ThreeIntegers([10, 8, 7, 5, 2, 1])

        self.assertEqual(Calc.find(), 10*8*7)


if __name__ == '__main__':
    unittest.main()
