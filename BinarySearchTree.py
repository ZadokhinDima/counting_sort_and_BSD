class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def insert(self, value):
        if self.search(value):
            return

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

        self.size += 1

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        if self.search(value):
            self.size -= 1
            self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def print_tree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, node, level = 0):
        if node is not None:
            self._print_recursive(node.right, level + 1)
            print('    ' * level + '->', node.value)
            self._print_recursive(node.left, level + 1)