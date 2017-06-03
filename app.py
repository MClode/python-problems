class StockCalculator:

    def __init__(self, list):
        if len(list) < 2:
            raise Exception("List needs more than one item!")
        self.list = list

    def check_for_loss(self):
        # Special case is when the list is a reverse sorted list (i.e. you are guaranteed to lose money)

        loss = self.list[1] - self.list[0]

        for key, val in enumerate(self.list):
            if key == 0:
                continue
            previous_val = self.list[key-1]
            if previous_val >= val:
                if (val - previous_val) > loss:
                    loss = val - previous_val
            else:
                return 1

        return loss

    # returns 6 (buying for $5 and selling for $11)
    def get_max_profit(self):

        sell, profit = 0, 0

        for i in self.list:
            buy = self.list.pop(0)
            for x in self.list:
                if x < buy or x < sell:
                    continue

                sell = x
                profit = x - buy

        return profit

    def find(self):
        loss = self.check_for_loss()
        if loss != 1:
            return loss
        else:
            return self.get_max_profit()

