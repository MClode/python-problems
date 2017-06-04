"""
You have a list of integers, and for each index you want to find the product of every integer except the integer
at that index.

Do not use division in your solution
"""


class ProductCalculator:

    def __init__(self, array):
        if len(array) < 2:
            raise Exception("The array needs more than one item!")
        self.array = array

    """
    O(n) solution using O(n) extra space (we need a copy of the list)
    """
    def find(self):

        products = self.array[:]
        running_total = 1

        # After one loop we have the product of all indexes that came before
        for key, value in enumerate(self.array):
            products[key] = running_total
            running_total = running_total * value

        running_total = 1
        # Now if we loop backwards from the end we can fill in the blanks, we should skip the last element because
        # it has already been completed
        for key, value in reversed(list(enumerate(self.array[:len(self.array)]))):
            products[key] = products[key] * running_total
            running_total = running_total * value

        return products