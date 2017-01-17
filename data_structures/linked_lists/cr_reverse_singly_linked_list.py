"""
Given a pointer/reference to the head of a singly linked list,
reverse it and return the pointer/reference to the head of reversed linked list.

Iterative and Recursive Solutions

[7, 14, 21, 28]
"""


def reverse_iterative(head):
    if head is None or head.prev_node is None:
        return head

    n = head.prev_node
    previous = head
    previous.prev_node = None

    while n is not None:
        temp = n
        n = n.prev_node
        temp.prev_node = previous
        previous = temp
    return previous


def reverse_recursive(head):
    if head is None or head.prev_node is None:
        return head

    reversed_list = reverse_recursive(head.prev_node)
    head.prev_node.prev_node = head
    head.prev_node = None
    return reversed_list
