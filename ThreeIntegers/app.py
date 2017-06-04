"""
Given a list of integers, find the highest product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""


class ThreeIntegers:

    def __init__(self, list):
        if len(list) < 3:
            raise Exception("The list needs at least three numbers!")
        self.list = list

    def find(self):
        max_product = 1

        return max_product
