class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_leaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False


def branch_sums(root):
    if root is None:
        return 0

    if is_leaf(root.left):
        left_sum = root.left.value
    else:
        left_sum = branch_sums(root.left)

    right_sum = branch_sums(root.right)

    return left_sum + right_sum


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.right = BinaryTree(7)
root.right.left = BinaryTree(15)
print("Sum of left leaves is", branch_sums(root))
