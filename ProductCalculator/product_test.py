import unittest

from ProductCalculator.app import ProductCalculator


class ProductCalculatorTest(unittest.TestCase):
    def test_product(self):
        Calc = ProductCalculator([1, 7, 3, 4])

        self.assertEqual(Calc.find(), [84, 12, 28, 21])

    def test_zero_values(self):
        Calc = ProductCalculator([0, 0, 0, 0])

        self.assertEqual(Calc.find(), [0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
