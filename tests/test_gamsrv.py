import unittest
from src.gamsrv import *

INF = float('inf')


class TestFindMinMaxLatwncy(unittest.TestCase):

    def test_1(self):
        N, M = 6, 6
        clients = {1, 2, 6}
        connections = [(1, 3, 10), (3, 4, 80), (4, 5, 50), (5, 6, 20), (2, 3, 40), (2, 4, 100)]
        expected_min_max_latency = 100

        min_max_latency = find_min_max_latency(M, N, clients, connections)
        self.assertEqual(min_max_latency, expected_min_max_latency)


    def test_2(self):
        N, M = 9, 12
        clients = {2, 4, 6}
        connections = [(1, 2, 20), (2, 3, 20), (3, 6, 20), (6, 9, 20), (9, 8, 20), (8, 7, 20), (7, 4, 20), (4, 1, 20),
                       (5, 2, 10), (5, 4, 10), (5, 6, 10), (5, 8, 10)]
        expected_min_max_latency = 10

        min_max_latency = find_min_max_latency(M, N, clients, connections)
        self.assertEqual(min_max_latency, expected_min_max_latency)


    def test_3(self):
        N, M = 3, 2
        clients = {1, 3}
        connections = [(1, 2, 50), (2, 3, 1000000000)]
        expected_min_max_latency = 1000000000

        min_max_latency = find_min_max_latency(M, N, clients, connections)
        self.assertEqual(min_max_latency, expected_min_max_latency)


if __name__ == "__main__":
    unittest.main()
