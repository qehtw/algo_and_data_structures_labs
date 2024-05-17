import unittest
from src.fsm_pattern_search import *


class TestSearch(unittest.TestCase):
    def test_1(self):
        needle_value = "abc"
        haystack_value = "abcabcabc"
        expected_match_index = [0, 3, 6]

        match_index = find_pattern_in_text(needle_value, haystack_value)
        self.assertEqual(expected_match_index, match_index)

    def test_2(self):
        needle_value = "shining"
        haystack_value = "Sun is shining"
        expected_match_index = [7]

        match_index = find_pattern_in_text(needle_value, haystack_value)
        self.assertEqual(expected_match_index, match_index)

    def test_3(self):
        needle_value = "oko"
        haystack_value = "okokokokoko"
        expected_match_index = [0, 2, 4, 6, 8]

        match_index = find_pattern_in_text(needle_value, haystack_value)
        self.assertEqual(expected_match_index, match_index)


    def test_4(self):
        needle_value = "ололо"
        haystack_value = "ололололо"
        expected_match_index = [0, 2, 4]

        match_index = find_pattern_in_text(needle_value, haystack_value)
        self.assertEqual(expected_match_index, match_index)


if __name__ == "__main__":
    unittest.main()
