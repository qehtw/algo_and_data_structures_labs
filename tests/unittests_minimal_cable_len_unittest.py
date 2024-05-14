import unittest
from minimal_cable_len import find_mst_lenght


class TestKraskal(unittest.TestCase):
    def test_1(self):
        matrix = [[0, 5, 7, 5, 10],
                  [5, 0, 9, 6, 20],
                  [7, 9, 0, 8, 5],
                  [5, 6, 8, 0, 7],
                  [10, 20, 5, 7, 0]]
        self.assertEqual(find_mst_lenght(matrix), 22)


    def test_2(self):
        matrix = [[0, 1, 4, 3],
                  [1, 0, 2, 1],
                  [4, 2, 0, 5],
                  [3, 1, 5, 0]]
        self.assertEqual(find_mst_lenght(matrix), 4)


    def test_3(self):
        matrix = [[0, 6, 0, 0, 2, 0, 0, 0],
                  [6, 0, 3, 0, 0, 0, 0, 4],
                  [0, 3, 0, 4, 0, 0, 3, 0],
                  [0, 0, 4, 0, 1, 3, 0, 0],
                  [2, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 3, 0, 0, 0, 0, 5],
                  [0, 4, 0, 0, 0, 2, 5, 0]]
        self.assertEqual(find_mst_lenght(matrix), 14)


if __name__ == "__main__":
    unittest.main()
