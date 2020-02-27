from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        elif value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)

        elif target < self.value:
            if self.left is not None:
                return self.right.contains(target)

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()

        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        my_q = Queue()
        my_q.enqueue(node)
        while my_q.len() > 0:
            temp = my_q.dequeue()
            print(temp.value)
            if temp.right is not None:
                my_q.enqueue(temp.right)
            if temp.left is not None:
                my_q.enqueue(temp.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        my_stack = Stack()
        my_stack.push(node)
        while my_stack.len() > 0:
            temp = my_stack.pop()
            print(temp.value)
            if temp.left is not None:
                my_stack.push(temp.left)
            if temp.right is not None:
                my_stack.push(temp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

        # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            print(node.value)
        if node.left is not None:
            node.left.pre_order_dft(node.left)
        if node.right is not None:
            node.right.pre_order_dft(node.right)

        # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            node.left.post_order_dft(node.left)
        if node.right is not None:
            node.right.post_order_dft(node.right)

        print(node.value)


# DFT Steps: (Stack)
# Initialize a stack
# Push root to stack
# while stack not empty
# Pop top item out of stack into temp
# Do something to it
# If temp has right put into stack
# If temp has left put into stack


# BFT Steps: (Queue)
# Initialize a Queue
# enqueue root to Queue
# while Queue not empty
# dequeue top item out of Queue into temp
# Do something to it
# If temp has right put into Queue
# If temp has left put into Queue
