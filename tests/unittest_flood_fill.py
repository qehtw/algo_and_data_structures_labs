import unittest
from flood_fill import flood_fill, is_valid


class TestFloodFill(unittest.TestCase):
    def test_is_valid(self):
        screen = [['W', 'W', 'B', 'B'],
                  ['W', 'W', 'B', 'B'],
                  ['B', 'B', 'B', 'B'],
                  ['B', 'B', 'B', 'B']]
        m, n = 4, 4
        self.assertTrue(is_valid(screen, m, n, 0, 0, 'W', 'G'))
        self.assertFalse(is_valid(screen, m, n, 0, 0, 'W', 'W'))
        self.assertFalse(is_valid(screen, m, n, -1, 0, 'W', 'G'))
        self.assertFalse(is_valid(screen, m, n, 0, 4, 'W', 'G'))

    def test_flood_fill(self):
        screen = [['W', 'W', 'B', 'B'],
                  ['W', 'W', 'B', 'B'],
                  ['B', 'B', 'B', 'B'],
                  ['B', 'B', 'B', 'B']]
        m, n = 4, 4
        x, y = 0, 0
        prev_color, new_color = 'W', 'G'
        expected_output = [['G', 'G', 'B', 'B'],
                           ['G', 'G', 'B', 'B'],
                           ['B', 'B', 'B', 'B'],
                           ['B', 'B', 'B', 'B']]
        self.assertEqual(flood_fill(screen, m, n, x, y, prev_color, new_color), expected_output)
