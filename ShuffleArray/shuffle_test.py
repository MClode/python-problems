import unittest

from ShuffleArray.app import ShuffleArray


class ShuffleArrayTest(unittest.TestCase):

  def setUp(self):
    self.original = [1, 2, 3, 4]
    self.shuffled = ShuffleArray(self.original[:]).run()

  def test_array_same_size(self):
    self.assertEqual(len(self.original), len(self.shuffled))

  def test_arrays_have_equivalent_content(self):
    """ Despite being terribly named, assertCountEqual actually does exactly what I need.
        It will assert that the items are equivalent, disregarding order. """
    self.assertCountEqual(self.original, self.shuffled)


if __name__ == '__main__':
  unittest.main()

