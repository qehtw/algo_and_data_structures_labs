import unittest

from src.sum_of_left_leafs import *


class TestBinaryTree(unittest.TestCase):
    def test_branch_sums_1(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.right = BinaryTree(7)
        root.right.left = BinaryTree(15)

        self.assertEqual(branch_sums(root), 24)

    def test_branch_sums_2(self):
        root = BinaryTree(20)
        root.left = BinaryTree(11)
        root.right = BinaryTree(24)
        root.left.right = BinaryTree(16)
        root.left.left = BinaryTree(2)
        root.left.right.right = BinaryTree(18)
        root.left.right.left = BinaryTree(13)

        self.assertEqual(branch_sums(root), 15)

    def test_branch_sums_3(self):
        root = BinaryTree(5)
        root.left = BinaryTree(4)
        root.right = BinaryTree(8)
        root.left.left = BinaryTree(2)
        root.right.left = BinaryTree(7)

        self.assertEqual(branch_sums(root), 9)


if __name__ == '__main__':
    unittest.main()
