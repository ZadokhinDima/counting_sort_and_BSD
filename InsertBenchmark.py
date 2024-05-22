from BinarySearchTree import BinarySearchTree
import random
import time
import matplotlib.pyplot as plt

bst = BinarySearchTree()

values_count = 10000
values = []

insert_times = {}

values.append(values_count * 5)

# Insert random elements into the binary search tree
for _ in range(values_count):
    values.append(random.randint(1, values_count * 10))

# Only unique values
values = list(set(values))

i = 0

for value in values:
    print(str(i))
    i += 1
    start = time.time()
    bst.insert(value)
    end = time.time()
    insert_times[value] = end - start

# Write values to file (separated by \n)
with open('c:/Users/dimaz/projects/projector/algoritms/values.txt', 'w') as file:
        file.write('\n'.join(map(str, insert_times)))

