import unittest

from robot_route import robot

class TestRobotFunc(unittest.TestCase):
    def test_robot_5_5(self):
        expected = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(robot(5, 5), expected)

    def test_value_4_2(self):
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(robot(4, 2), expected)

    def test_value_1_6(self):
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(robot(1, 6), expected)


if __name__ == '__main__':
    unittest.main()
