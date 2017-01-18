"""
Given a pointer/reference to the head of a singly linked list,
reverse it and return the pointer/reference to the head of reversed linked list.

Iterative and Recursive Solutions

[7, 14, 21, 28]
"""


class LinkedList:

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

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def reverse_iterative(head):
    if head is None or head.next_node is None:
        return head

    n = head.next_node
    previous = head
    previous.next_node = None

    while n is not None:
        temp = n
        n = n.next_node
        temp.next_node = previous
        previous = temp
    return previous


def reverse_recursive(head):
    if head is None or head.next_node is None:
        return head

    reversed_list = reverse_recursive(head.next_node)
    head.next_node.next_node = head
    head.next_node = None
    return reversed_list


def setUp():
    l = LinkedList()
    l.insert(7)
    l.insert(14)
    l.insert(21)
    l.insert(28)
    return l

if __name__ == '__main__':
    l = setUp()
    print(reverse_recursive(l.head).data)
    print(reverse_iterative(l.head).data)
