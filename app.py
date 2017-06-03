class StockCalculator:

    def __init__(self, list):
        if len(list) < 2:
            raise Exception("The list needs more than one item!")
        self.list = list

    def find(self):

        min_price = self.list[0]
        max_profit = self.list[1] - self.list[0]

        # We need to iterate over the list just once to get O(n). We will always know our highest profit by simply
        # keeping track of profit and the lowest previous price. If the current price gives us a better profit, we
        # update max profit. A simple greedy algorithm
        for price in self.list[1:]:
            max_profit = max((price - min_price), max_profit)

            min_price = min(price, min_price)

        return max_profit