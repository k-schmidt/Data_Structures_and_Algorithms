"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""


class LinkedList:

    class Node:

        def __init__(self, data, next_node):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert(self, x):
        new_node = self.Node(x, self.head)
        self.head = new_node
        self.size += 1

    def delete(self):
        if self.is_empty():
            raise Exception("underflow")
        answer = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        return answer


def setUp():
    linked_list = LinkedList()
    for x in range(1, 10):
        linked_list.insert(x)
    for x in range(1, 10):
        linked_list.insert(x)
    return linked_list


def remove_duplicates(linked_list):
    hash_table = []
    node = linked_list.head
    while node.next_node is not None:
        if node.data in hash_table:
            node = node.next_node
        else:
            hash_table.append(node.data)
    return hash_table


def remove_duplicates2(node):
    hash_table = []
    previous = LinkedList.Node(None, None)
    while node is not None:
        if node.data in hash_table:
            previous.next_node = node.next_node
        else:
            hash_table.append(node.data)
            previous = node
        node = node.next_node

if __name__ == '__main__':
    linked_list = setUp()
    print(linked_list.size)
    print(remove_duplicates(linked_list))
