class Node:
    def __init__(self, value=None):
        self.value = value
        self.l_child = None
        self.r_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.l_child is None:
                cur_node.l_child = Node(value)
            else:
                self._insert(value, cur_node.l_child)
        elif value > cur_node.value:
            if cur_node.r_child is None:
                cur_node.r_child = Node(value)
            else:
                self._insert(value, cur_node.r_child)
        else:
            print("Value already in tree!")

    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        else:
            left_height = self._height(cur_node.l_child, cur_height + 1)
            right_height = self._height(cur_node.r_child, cur_height + 1)
            return max(left_height, right_height)

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, cur_node):
        if cur_node.value == value:
            return True
        elif value > cur_node.value and cur_node.r_child is not None:
            return self._search(value, cur_node.r_child)
        elif value < cur_node.value and cur_node.l_child is not None:
            return self._search(value, cur_node.l_child)
        else:
            return False

    def print_tree(self):
        if self.root is None:
            print("Tree empty!")
        else:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.l_child)
            print(cur_node.value)
            self._print_tree(cur_node.r_child)


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_element = randint(0, max_int)
        tree.insert(cur_element)
    return tree


tree = BST()
# fill_tree(tree)
tree.insert(0)
tree.insert(4)
tree.insert(7)
tree.insert(3)
tree.insert(11)
tree.insert(15)
tree.insert(13)
tree.insert(10)
tree.insert(19)
tree.insert(31)

tree.print_tree()
print(tree.height())
print(tree.search(7))
print(tree.search(27))
