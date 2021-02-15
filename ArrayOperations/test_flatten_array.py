"""
The below test cases are implemented for flatten_array.py

Author: Mounish Kokkula
Edit: version #1
Date: Feb 15th 2021
"""


import unittest
from flatten_array import ArrayOperations


class MyTestCase(unittest.TestCase):
    def test_flatten_array1(self):
        fa = ArrayOperations()
        self.assertEqual(fa.array_handler([1, 2, [3, [4, 5]], 6]), [1, 2, 3, 4, 5, 6])

    def test_flatten_array2(self):
        fa = ArrayOperations()
        self.assertEqual(fa.array_handler([1, 2, [3], [[4, 5]], 6]), [1, 2, 3, 4, 5, 6])

    def test_flatten_array3(self):
        fa = ArrayOperations()
        self.assertEqual(fa.array_handler([1, 2, [3, [4, [5, [6, [7, [8]]]]]], 9, [10, 11, [12, 13, [14, 15, [16, [17, [18, [19, [20]]]]]]]]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_notString(self):
        fa = ArrayOperations()
        self.assertEqual(fa.array_handler([1, 2, ['3'], [[4, 5]], 6]), "Not a integer. Check Input!")

    def test_notDictionary(self):
        fa = ArrayOperations()
        self.assertEqual(fa.array_handler([1, 2, {3: 4}, [[4, 5]], 6]), "Not a integer. Check Input!")

    def test_notTuple(self):
        fa = ArrayOperations()
        self.assertEqual(fa.array_handler([1, 2, (3, 4), [[4, 5]], 6]), "Not a integer. Check Input!")


if __name__ == '__main__':
    unittest.main()
