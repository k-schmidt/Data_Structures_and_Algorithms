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
Unlike an array in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object.

Each element (we will call it a **node**) of a list is comprising of two items - the data and a reference to the next node.
The last node has a reference to null.
The entry point into a linked list is called the **head** of the list.
It should be noted that head is not a separate node, but the reference to the first node.
If the list is empty then the head is a null reference.

A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand.
**Any application which has to deal with an unknown number of objects will need to use a linked list.**

One **disadvantage** of a linked list against an array is that it does not allow direct access to the individual elemants. If you want to access a particular item then you have to start at the head and follow the references until you get to that item. O(n)

Another **disadvantage** is that a linked list uses more memory compare with an array - extra 4 bytes to store a reference to the next node.

A **doubly linked list** is a list that has two references, one to the next node and another to previous node.
A **circular linked list** is a list where the last node of the list points back to the first node (or head) of the list.

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

``` python
class LinkedList:

    class Node:

        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, x):
        self.head = self.Node(x, self.head)

    def iterate(self):
        if self.head is None:
            return
        node = self.head
        while node.data is not None:
            node = node.next_node

    def add_last(self, x):
        if self.head is None:
            self.add_first(x)
        else:
            tmp = self.head
            while tmp.data is not None:
                tmp = tmp.next_node
            tmp.next_node = self.Node(x)

    def insert_after(self, key, x):
        tmp = self.head
        while tmp is not None and tmp.data != key:
            tmp = tmp.next_node
        if tmp is not None:
            tmp.next_node = Node(x, tmp.next_node)

    def insert_before(self, key, x):
        if self.head is None:
            return
        if self.head.data == key:
            self.add_first(x)
            return
        tmp = self.head
        prv = None
        while tmp is not None and tmp.data != key:
            prv = tmp
            tmp = tmp.next_node
        if tmp is not None:
            prv.next_node = self.Node(x, tmp)

    def delete(self, key):
        if self.head is None:
            raise Exception("underflow")
        if self.head.data == key:
            self.head = self.head.next_node
            return
        tmp = self.head
        prv = None
        while tmp is not None and tmp.data != key:
            prv = tmp
            tmp = tmp.next_node
        if tmp is None:
            raise Exception("underflow")
        prv.next_node = tmp.next_node
```

## Representing Rooted Trees
We represent each node of a tree by an object.
As with linked lists, we assume that each node contains a *key* attribute.
The remaining attributes of interest are pointers to other nodes, and they vary according to the type of tree.

**Binary trees**
Each node has *p*, *left*, and *right* to store pointers to the parent, left child, and right child.
If `x.p = NIL`, then x is the root.
If node x has no left child, then `x.left = NIL`, and similarly for the right child.
The root of the entire tree T is pointed to by the attribute `T.root`. If `T.root = NIL`, then the tree is empty.

**Rooted trees with unbounded branching**
The **left-child, right-sibling representation** has the advantage of using only O(n) space for any n-node rooted tree.
As before, each node contains a parent pointer `p`, and T.root points to the root of tree T.
Instead of having a pointer to each of its children, however, each node x has only two pointers:


1. `x.left-child` points to the leftmost child of node x, and
2. `x.right-sibling` points to the sibling of x immediately to its right.

If node x has no children, then `x.left-child = NIL` and if node x is the rightmost child of its parent, then `x.right-sibling = NIL`.
