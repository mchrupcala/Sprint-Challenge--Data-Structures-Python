import time
import sys
from binary_search_tree import BinarySearchTree

# Runtime complexity is: O(n^2) since there's a nested for loop.

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


newtree = BinarySearchTree(names_1[0])
tree = BinarySearchTree(names_1[0])
for x in names_1[1:]:
    tree.insert(x)



duplicates = []
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)

print(duplicates)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
