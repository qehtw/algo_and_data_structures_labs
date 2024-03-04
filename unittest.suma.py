import unittest

from sem2.lab2.suma import suma

__import__(suma)


class TestFindSum(unittest.TestCase):
    def test_valid_sum_exists(self):
        new_arr = [1, 2, 3, 6]
        goal = 6
        self.assertTrue(suma(new_arr, goal))


if __name__ == '__main__':
    unittest.main()
