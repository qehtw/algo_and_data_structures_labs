import unittest

from red_black_priority_queue import RedBlackTree, Node
import unittest


class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.rbt = RedBlackTree()

    def test_insert(self):
        # Test inserting nodes into an empty tree
        self.rbt.insert(10, 1)
        self.assertEqual(self.rbt.root.val, 10)
        self.assertEqual(self.rbt.root.color, 0)  # Root should be black

        # Test inserting nodes into a non-empty tree
        self.rbt.insert(5, 2)
        self.rbt.insert(15, 3)
        self.assertEqual(self.rbt.root.left.val, 5)
        self.assertEqual(self.rbt.root.right.val, 15)

    def test_search(self):
        # Test searching in an empty tree
        self.assertIsNone(self.rbt.search())

        # Test searching in a non-empty tree
        self.rbt.insert(10, 1)
        self.rbt.insert(5, 2)
        self.rbt.insert(15, 3)
        self.rbt.insert(3, 4)
        self.assertEqual(self.rbt.search().val, 3)

    def test_delete(self):
        # Test deleting from an empty tree
        self.assertIsNone(self.rbt.delete())

        # Test deleting from a non-empty tree
        self.rbt.insert(10, 1)
        self.rbt.insert(5, 2)
        self.rbt.insert(15, 3)
        self.rbt.insert(3, 4)
        self.assertEqual(
            self.rbt.delete(), 2
        )  # Deleting node with minimum priority (5)
        self.assertIsNone(self.rbt.root.left)


if __name__ == "__main__":
    unittest.main()
