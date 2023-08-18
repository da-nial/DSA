from random import randint


class Node:
    def __init__(self, value, parent, left_child=None, right_child=None):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class BST:
    """
    Anything in the left subtree less or equal,
    Anything in the right subtree *strictly* bigger
    """

    def __init__(self, root_value):
        self.root = Node(root_value, None)
        self.size = 1

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None)

        cur_node = self.root

        while True:
            if value <= cur_node.value:
                if cur_node.left_child is None:
                    cur_node.left_child = Node(value, cur_node)
                    break
                else:
                    cur_node = cur_node.left_child
            else:
                if cur_node.right_child is None:
                    cur_node.right_child = Node(value, cur_node)
                    break
                else:
                    cur_node = cur_node.right_child

        self.size += 1

    def print(self):
        queue = [self.root, ]
        nodes = []

        while queue:
            cur_node = queue.pop(0)

            nodes.append(cur_node)

            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)
            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

        i = 0
        while i < self.size:
            values = [node.value for node in nodes[i:2 * i + 1]]
            print(values)
            i = 2 * i + 1

    def zprint(self):
        cur_node = self.root
        self._zprint(self.root)

    def _zprint(self, root):
        # convert to traverse
        if root.left_child is not None:
            self._zprint(root.left_child)

        print(root.value)

        if root.right_child is not None:
            self._zprint(root.right_child)

    def fill_tree(self, num_new_nodes):
        if self.root is None:
            value = randint(1, 100)
            self.root = Node(value, None)

        for i in range(num_new_nodes):
            value = randint(1, 100)
            self.insert(value)


tree = BST(10)

tree.fill_tree(15)
# tree.print()

# tree.insert(10)
# tree.insert(51)
# tree.insert(3)
# tree.insert(41)
# tree.insert(89)
# tree.insert(20)

tree.zprint()
