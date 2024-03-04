import unittest

from Lab2 import suma



class TestFindSum(unittest.TestCase):
    def test_valid_sum_exists(self):
        new_arr = [1, 2, 3, 6]
        goal = 6
        self.assertTrue(suma(new_arr, goal))

    def test_valid_sum_exists(self):
        new_arr = [1, 3, 5, 6]
        goal = 9
        self.assertTrue(suma(new_arr, goal))

    def test_valid_sum_exists(self):
        new_arr = [2, 4, 8, 15]
        goal = 14
        self.assertTrue(suma(new_arr, goal))



if __name__ == '__main__':
    unittest.main()

