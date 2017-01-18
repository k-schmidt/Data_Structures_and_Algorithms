"""
Implement a queue by a singly linked list L. The operations ENQUEUE and DEQUEUE should still take O(1) time.
"""


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedQueue:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, x):
        new_node = Node(x, self.head)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("underflow")
        answer = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer
