import BinarySearchTree

bst = BinarySearchTree()

# Insert random elements into the binary search tree
for _ in range(10):
    value = random.randint(1, 100)
    bst.insert(value)