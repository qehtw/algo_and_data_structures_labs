class Node:
    def __init__(self, val, priority, color=0):
        self.val = val
        self.priority = priority
        self.color = 1
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, val, priority):
        node = Node(val, priority)
        if self.root is None:
            self.root = node
            self.root.color = 0
            return

        parent = None
        current = self.root
        while current:
            parent = current
            if priority < current.priority:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if priority < parent.priority:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent and node.parent.color == 1:
            if node.parent.parent:
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    if uncle and uncle.color == 1:
                        node.parent.color = 0
                        uncle.color = 0
                        node.parent.parent.color = 1
                        node = node.parent.parent
                    else:
                        if node == node.parent.right:
                            node = node.parent
                            self.rotate_left(node)
                        node.parent.color = 0
                        node.parent.parent.color = 1
                        self.rotate_right(node.parent.parent)
                else:
                    uncle = node.parent.parent.left
                    if uncle and uncle.color == 1:
                        node.parent.color = 0
                        uncle.color = 0
                        node.parent.parent.color = 1
                        node = node.parent.parent
                    else:
                        if node == node.parent.left:
                            node = node.parent
                            self.rotate_right(node)
                        node.parent.color = 0
                        node.parent.parent.color = 1
                        self.rotate_left(node.parent.parent)
            else:  # If node.parent.parent is None, set root's color to black
                self.root.color = 0
                break

        self.root.color = 0

    def fix_delete(self, node):
        if node is None:
            return

        while node != self.root and (node is None or node.color == 0):
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 1:
                    sibling.color = 0
                    node.parent.color = 1
                    self.rotate_left(node.parent)
                    sibling = node.parent.right

                if (sibling.left is None or sibling.left.color == 0) and (
                        sibling.right is None or sibling.right.color == 0
                ):
                    sibling.color = 1
                    node = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.rotate_right(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = 0
                    if sibling.right:
                        sibling.right.color = 0
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 1:
                    sibling.color = 0
                    node.parent.color = 1
                    self.rotate_right(node.parent)
                    sibling = node.parent.left  # Corrected line

                if (sibling.right is None or sibling.right.color == 0) and (
                        sibling.left is None or sibling.left.color == 0
                ):
                    sibling.color = 1
                    node = node.parent
                else:
                    if sibling.left is None or sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.rotate_left(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 0
                    if sibling.left:
                        sibling.left.color = 0
                    self.rotate_right(node.parent)
                    node = self.root

    def delete(self):
        if self.root is None:
            return

        node = self.root
        while node.left:
            node = node.left

        self.delete_node(node)
        return node.val, node.priority

    def delete_node(self, node):
        if node is None:
            return

        if node.left is None or node.right is None:
            self.delete_one_child(node)
        else:
            successor = self.get_successor(node)
            node.val, node.priority = successor.val, successor.priority
            self.delete_one_child(successor)

    def delete_one_child(self, node):
        child = node.left if node.left else node.right
        if child:
            child.parent = node.parent
        if node.parent is None:
            self.root = child
        else:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child

        if node.color == 0:
            self.fix_delete(child)

    def search(self):
        node = self.root

        while node and node.left:
            node = node.left

        return node

    def __parent_is_left_child(self, node):
        if node.parent.parent is None:
            return
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
        if node.parent.parent is None:
            return
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

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_tree(self):
        self._inorder_tree(self.root)

    def _inorder_tree(self, node):
        if node is None:
            return

        self._inorder_tree(node.left)
        print(node.val, node.priority, node.color)
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
