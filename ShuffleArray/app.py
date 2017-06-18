"""
Write a function for doing an in-place ↴ shuffle of a list.
The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
"""

from random import randint

class ShuffleArray:

  def __init__(self, l):
    self.l = l

  def get_random(self, floor, ceiling):
    return randint(floor, ceiling)

  def run(self):

    i = 0
    while i < len(self.l):
      key = self.get_random(i, len(self.l)-1)

      self.l[i], self.l[key] = self.l[key], self.l[i]

      i += 1

    return self.l

