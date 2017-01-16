"""
Singly Linked List
"""


class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size


class Headed(LinkedList):

    def __init__(self, head=None):
        super().__init__(head)

    def insert(self, new_head):
        new_node = Node(new_head)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1


class Tailed(LinkedList):

    def __init__(self, tail=None):
        super().__init__(tail)

    def append(self, new_head):
        new_node = Node(new_head)
        new_node.next = None
        self.head.next = new_node
        self.head = new_node
        self.size += 1
