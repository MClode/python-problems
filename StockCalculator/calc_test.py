import unittest

from StockCalculator.app import StockCalculator


class StockCalculatorTest(unittest.TestCase):
    def test_loss(self):
        Calc = StockCalculator([10, 8, 7, 5, 2, 1])

        self.assertEqual(Calc.find(), -1)

    def test_profit(self):
        Calc = StockCalculator([10, 7, 5, 8, 11, 9])

        self.assertEqual(Calc.find(), 6)

    def test_no_profit(self):
        Calc = StockCalculator([10, 10, 10, 10, 10, 10])

        self.assertEqual(Calc.find(), 0)


if __name__ == '__main__':
    unittest.main()
