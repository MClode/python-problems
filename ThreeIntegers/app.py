"""
Given a list of integers, find the highest product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""


class ThreeIntegers:

    def __init__(self, list):
        if len(list) < 3:
            raise Exception("The list needs at least three numbers!")
        self.positive_integers = [0, 0, 0]
        self.negative_integers = [0, 0]
        self.list = list

    def find(self):
        for number in self.list:
            if number > 0:
                self.positive_numbers(number, self.positive_integers)
            if number < 0:
                self.negative_numbers(number, self.negative_integers)

        return max(
            self.positive_integers[0]*self.positive_integers[1]*self.positive_integers[2],
            self.negative_integers[0]*self.negative_integers[1]*self.positive_integers[0],
        )

    def positive_numbers(self, n, list):
        if n > list[0]:
            list[1] = max(list[0], list[1])
            list[2] = max(list[1], list[2])
            list[0] = n
            return
        if n > list[1]:
            list[2] = max(list[1], list[2])
            list[1] = n
            return
        if n > list[2]:
            list[2] = n
            return

    def negative_numbers(self, n, list):
        if n < list[0]:
            list[1] = min(list[0], list[1])
            list[0] = n
            return
        if n < list[1]:
            list[1] = n
            return
