# Introduction to a Heap

## The Basics

We can implement a Heap as either a tree or an array.
We will be implementing a tree first, particularly a binary tree where each node has at most two children.
We start with the root node and start filling this heap from left to right.
The first child of the root is assigned the left child.
The second child of the root is assigned the right child.
Continue filling in from top to bottom, left to right.
We don't move on to the row below until the row above is completely full.


### Types

We either deal with two types of Heaps:
1. Max Heap
    2. Any parent node is going to have a value greater than or equal to its children.
2. Min Heap
    3. Any parent node is going to have a value less than or equal to its children.


When we want to add an item that violates the rule, we have to compare its value to the parent and flip their positions.


### Algorithm for adding values to a Max Binary Tree Heap

1. First add item to the bottom-most, left-most position.
2. Compare its value versus its parent.
3. If the value of the new child is greater than its parent then switch the two nodes.
4. Continue checking every parent until the root.


## Removing an Item from a Heap

1. First find node to remove.
2. Take the bottom-most, left-most node and replace it with the positon of the removed node.
3. But now the parent is smaller than both of its children.
4. Compare the two children nodes and find out which is the biggest.
5. Swap the current parent with the largest of the children.
6. Continue until the small node is in its correct position.

## Describing a Heap as an Array

1. The root of the Heap goes in index 0 of Array.
2. Go down the tree from left to right to fill in the values.
    3. But how do parents know what children they have in a flat array and vice versa?
        4. Parent n has children `2n +1` and `2n + 2` where n is the index of the array.
        5. Child n has parent `(n-1) // 2` where n is the index of the array.
