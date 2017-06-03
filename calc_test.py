import unittest
from app import StockCalculator


class MyTestCase(unittest.TestCase):
    def test_loss(self):
        Calc = StockCalculator([10, 8, 7, 5, 2, 1])

        self.assertEqual(Calc.find(), -1)

    def test_profit(self):
        Calc = StockCalculator([10, 7, 5, 8, 11, 9])

        self.assertEqual(Calc.find(), 6)


if __name__ == '__main__':
    unittest.main()
