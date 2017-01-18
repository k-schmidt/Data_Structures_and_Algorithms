"""
Implement a stack using a singly linked list L. The operations PUSH and POP should still take O(1) time.
"""


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedStack:

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        """
        Max size?
        """
        new_node = Node(x, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("underflow")
        answer = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        return answer
