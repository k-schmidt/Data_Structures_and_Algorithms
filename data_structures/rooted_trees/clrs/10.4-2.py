"""
Write and O(n) time recursive procedure that, given an n-node binary tree, prints out the key of each node in the tree.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_key_recur(node):
    if node.data is None:
        return

    print(node.data)
    print_key_recur(node.left)
    print_key_recur(node.right)
