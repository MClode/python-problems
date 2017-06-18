import unittest

from ShuffleArray.app import ShuffleArray


class ShuffleArrayTest(unittest.TestCase):
    def test_array_same_size(self):
        shuffle = ShuffleArray()
        input = [1, 7, 3, 4]
        res = shuffle.run(input[:])

        self.assertEqual(len(input), len(res))


if __name__ == '__main__':
    unittest.main()
