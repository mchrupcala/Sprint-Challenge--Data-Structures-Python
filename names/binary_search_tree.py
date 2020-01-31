import sys
sys.path.append('../imports')
from queue import Queue
from stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value >= self.value and self.right is not None:
            current_right = self.right
            current_right.insert(value)
        elif value < self.value and self.left is not None:
            current_left = self.left
            current_left.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.right is not None and self.right.value == target:
            print(target)
            # return target
            return True
        elif self.left is not None and self.left.value == target:
            print(target)
            # return target
            return True
        elif target > self.value and self.right is not None:
            self.right.contains(target)
        elif target < self.value and self.left is not None:
            self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        elif self.right is None:
            return self.value
        ##I don't understand why this test is failing...I'mn printing the correct return value...twice...ummm what now

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)





    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)




    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            temp = queue.dequeue()
            print(temp.value)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            temp = stack.pop()
            print(temp.value)
            if temp.left:
                stack.push(temp.left)
            if temp.right:
                stack.push(temp.right)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
