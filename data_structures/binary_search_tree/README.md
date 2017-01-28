# Introduction to Binary Search Tree


## Components

A tree is made of up `Nodes` that have values and pointers to their child `Nodes`.

## Node Properties

``` python
class Node

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
```

## Binary Search Tree Properties

All of the nodes below the node's left pointer will be less than its data.
All of the nodes below the node's right pointer will be greater than its data.

- **Root**
    - Pointer that points to the top of the tree
- **Parent**
    - Describes the relationship between two nodes.
- **Child**
    - A descendant of a parent node
- **Leaf**
    - A leaf node is a node that does not have **any** children, therefore its left and right attributes are `null`.


## Adding Nodes to Binary Search Tree

### Algorithm

1. Start at the top. If the tree is empty then the first node is the root. Otherwise, see if it is less than or greater than the node.
2. If the new node is greater than the node in question, then it becomes the node's right child.
3. If the new node is less than the node in question, then it becomes the node's left child.
4. Repeat
