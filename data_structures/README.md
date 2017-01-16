# Data Structures

## Stacks and Queues

**Stack**: The element deleted from the set is the one most recently inserted: the stack implements, **last-in, first-out,** or **LIFO** policy.

**Queue:** The element deleted is always the one that has been in the set for the longest time: the queue implements **first-in, first-out** of **FIFO** policy.

``` python
## Stack
## Each of the three stack operations takes O(1) time

class Stack:

    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size
        self.size = len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, x):
        if self.max_size is not None and self.size < self.max_size:
            self.items.append(x)
        elif self.max_size is not None and self.size == self.max_size:
            raise Exception("overflow")
        else:
            self.items.append(x)

    def pop(self):
        if self.is_empty():
            raise Exception("underflow")
        return self.items.pop()
```


``` python
## Queue


class Queue:

    def __init__(self, max_size=None):
        self.items = []
        self.size = len(self.items)
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, x):
        if self.max_size is not None and self.size < self.max_size:
            self.items.append(x)
        elif self.max_size is not None and self.size == self.max_size:
            raise Exception("overflow")
        else:
            self.items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise Exception("underflow")
        return self.items.pop(0)
```

**Linked List:** a data structure in which the objects are arranged in a linear order.
Unlike an arry in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object.

**Forms:**
+ Either singly linked or doubly linked
    + Singly linked?
        + Omit the *prev* pointer in each element
+ Sorted or unsorted
    + Sorted?
        + The linear order of the list corresponds to the linear order of keys stored in elements of the list; the minimum element is then the head of the list and the maximum element is the tail.
+ Circular or not circular
    + Circular?
        + The *prev* pointer of the head of the list points to the tail, and the *next* pointer of the tail of the list points to the head.

``` python
## Unsorted Doubly Linked List

class Node:

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size  = 0

    def get_size(self):
        return self.size

    def search(self, k):
        x = self.head
        while x is not None and x.data != k:
            x = x.next_node
        return x

    def insert(self, new_head):
        new_node = Node(new_head)
        new_node.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(new_node)
        self.head = new_node
        new_node.set_prev(None)
        self.size += 1

    def delete(self, x=None):
        if self.head is None:
            raise Exception("underflow")
        elif x is None:
            self.head = self.head.next_node
            if self.head is not None:
                self.head.prev_node = None
        else:
            node = self.search(x)
            if node.prev_node is not None:
                node.prev_node.next_node = node.next_node
            else:
                self.head = node.next_node
                self.head.prev_node = None
            if node.next_node is not None:
                node.next_node.prev_node = node.prev_node
```


``` python
## LinkedStack
## LIFO Stack implementation using a singly linked list for storage

class LinkedStack:

    class Node:

        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        new_node = self.Node(x, self.head)
        self.head = new_node
        self.size += 1

    def top(self):
        if self.is_empty():
            raise Exception("empty stack")
        return self.head.data

    def pop(self):
        if self.is_empty():
            raise Exception("underflow")
        answer = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        return answer
```

``` python
## LinkedQueue
## Implementing a Queue using a singly linked list


class LinkedQueue

    class Node:

        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node


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
```
