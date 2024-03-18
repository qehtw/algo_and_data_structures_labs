class Node:
    def __init__(self, val, priority, color=1):
        self.val = val
        self.priority = priority
        self.color = color
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert_fix(self, node):
        while node.parent and node.parent.color == 1:
            if node.parent.left == node.parent:
                self.__parent_is_left_child(node)
            else:
                self.__parent_is_right_child(node)
            if node == self.root:
                break
            self.root.color = 0

    def insert(self, val, priority):
        node = Node(val, priority)
        root = self.root
        current_node = None

        if self.root is None:
            self.root = Node(val, priority, color=0)
            return

        while root is not None:
            current_node = root
            if root.priority is None or priority >= root.priority:
                root = root.left
            else:
                root = root.right

        node.parent = current_node

        if current_node is None:
            self.root = node
        elif priority >= current_node.priority:
            current_node.left = node
        else:
            current_node.right = node

        self.insert_fix(node)

    def delete_fix(self, root):
        while root != self.root and root.color == 0:
            if root == root.parent.left:
                sibling = root.parent.right

                if sibling.color == 1:
                    sibling.color = 0
                    root.parent.color = 1
                    self.left_rotate(root.parent)
                    sibling = root.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    root = root.parent
                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.right_rotate(sibling)
                        sibling = root.parent.right

                    sibling.color = root.parent.color
                    root.parent.color = 0
                    sibling.right.color = 0
                    self.left_rotate(root.parent)
                    root = self.root
            else:
                pass

        root.color = 0

    def delete(self):
        node = self.search()
        node_to_delete = node
        a_color = node.color

        if node.left is None:
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            if node.right is not None:
                node.right.parent = node.parent
            node = node.right
        if a_color == 0:
            self.delete_fix(node)
        return node_to_delete.priority

    def search(self):
        node = self.root

        while node.left:
            node = node.left

        return node

    def __parent_is_left_child(self, node):
        if node.parent.parent.right and node.parent.parent.right.color == 1:
            node.parent.color = 0
            node.parent.parent.right.color = 0
            node.parent.parent.color = 1
            node = node.parent.parent
        else:
            if node == node.parent.right:
                node = node.parent
                self.left_rotate(node)
            node.parent.color = 0
            node.parent.parent.color = 1
            self.right_rotate(node.parent.parent)

    def __parent_is_right_child(self, node):
        if node.parent.parent.left and node.parent.parent.left.color == 1:
            node.parent.parent.left.color = 0
            node.parent.color = 0
            node.parent.parent.color = 1
            node = node.parent.parent
        else:
            if node == node.parent.left:
                node = node.parent
                self.right_rotate(node)
            node.parent.color = 0
            node.parent.parent.color = 1
            self.left_rotate(node.parent.parent)

    def left_rotate(self, root):
        current_node = root.right
        root.right = current_node.left
        current_node.parent = root.parent

        if current_node.left is not None:
            current_node.left.parent = root

        if root.parent is None:
            self.root = current_node
        elif root == root.parent.left:
            root.parent.left = current_node
        else:
            root.parent.right = current_node

        current_node.left = root
        root.parent = current_node

    def right_rotate(self, root):
        current_node = root.left
        root.left = current_node.right
        current_node.parent = root.parent

        if current_node.right is not None:
            self.root = current_node
        elif root == root.parent.left:
            root.parent.left = current_node
        else:
            root.parent.right = current_node

        current_node.right = root
        root.parent = current_node

    def inorder_tree(self):
        self._inorder_tree(self.root)

    def _inorder_tree(self, node):
        if node is None:
            return

        self._inorder_tree(node.left)
        print(node.color)
        print(node.priority)
        self._inorder_tree(node.right)

    def __printCall(self, node, indent, last):
        if node:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            print(str(node.val) + "(" + str(node.color) + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    def print_tree(self):
        self.__printCall(self.root, "", True)


if __name__ == "__main__":
    rbt = RedBlackTree()

    rbt.insert(55, 1)
    rbt.insert(40, 2)
    rbt.insert(65, 3)
    rbt.insert(60, 4)
    rbt.insert(75, 5)
    rbt.insert(57, 6)

    rbt.print_tree()

print("Tree after insertions:")
rbt.inorder_tree()
print()

# Delete a node
deleted_priority = rbt.delete()
print(f"Deleted node with priority: {deleted_priority}")
print("Tree after deletion:")
rbt.inorder_tree()
print()

# Search for the node with minimum priority
min_node = rbt.search()
if min_node:
    print(
        f"Node with minimum priority: Value: {min_node.val}, Priority: {min_node.priority}, Color: {min_node.color}"
    )
else:
    print("Tree is empty")
