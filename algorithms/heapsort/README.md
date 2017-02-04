# Heapsort

The (binary) heap data structure is an array object that we can view as a nearly complete binary tree.
An array A that represents a heap is an object with two attributes:


1. A.length
2. A.heap-size


The most natural implementation of this binary tree would store each key in a node with pointers to its two children.
As with binary search trees, the memory used by the pointers can easily outweigh the size of keys.
The heap os a data structure that enables us to represent binary trees without using any pointers.


Space efficiency thus demands that we not allow holes in our tree, that each level be packed as much as it can be.
Only the last level may be incomplete.


How can we efficiently search for a particular key in a heap?


We can't. Binary search does not work because a heap is not a binary search tree.
We can do linear search though.


We can find nodes within the array using the equations:

``` text
Parent(i):
    return (n-1) // 2

Left Child(i):
    return (2n + 1)

Right Child(i):
    return 2n + 2
```


In a **max-heap** the largest element is stored at the root and the subtree rooted at a node containes values no larger than that contained at the node itself.


We shall see that basic operations on heaps run in time at most proportional to the height of the tree and thus take **O(lgn)** time.

## Maintaining the heap property (MAX-HEAPIFY)

When it is called, Max-Heapify assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are max-heaps, but that A[i] might be smaller than its children, thus violating the max-heap property.


``` text
MAX-HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l <= A.heap-size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap-size and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange A[i] with A[largest]
        MAX-HEAPIFY(A, largest)
```


The children's subtrees each have size at most 2n/3 - the worst case occurs when the bottom level of the tree is exactly half full - and therefore we can describe the running time by the recurrence:


``` text
T(n) <= T(2n/3) + Omega(1)
```

The solution to this recurrence by case 2 of the master theorem is:

``` text
T(n) = O(lgn)
```

## Build Max Heap

Add nodes from left to right until you've built a tree.
Then call Build-Max-Heap to turn the tree into a max-heap.

``` text
BUILD-MAX-HEAP(A):
    A.heap-size = A.length
    for i in range(A.length // 2, 1, -1):
        MAX-HEAPIFY(A, i)
```

Each call to MAX-HEAPIFY costs O(lgn) time and BUILD-MAX-HEAP makes O(n) calls.
Thus the running time is O(nlgn)

## The Heapsort Algorithm

The heapsort algorithm starts by using BUILD-MAX-HEAP to build a max-heap on the input array A where n = A.length.
Since the maximum element of the array is stored at the root A[1], we can put it into its correct final position by exchanging it with A[n].
We discard node n from the heap by reducing the heap-size of the array by 1 (A.heap-size - 1), but the new root might violate the Max Heap property so we call MAX-HEAPIFY to ensure a Max Heap each time.

``` text
HEAPSORT(A)
    BUILD-MAX-HEAP(A)
    for i in range(A.length, 2, -1):
        exchange A[1] with A[i]
        A.heap-size -= 1
        MAX-HEAPIFY(A, 1)
```

The **Heapsort** procedure takes **O(nlgn)**, since the call to BUILD-MAX-HEAP takes time O(n) and each of the n - 1 calls to MAX-HEAPIFY takes O(lgn).

## Priority Queues

A priority queue is a data structure for maintaining a set S of elements, each with an associated value called a key.


A **max-priority queue** supports the following operations:

1. Insert(S, x)
2. Maximum(S)
3. Extract-Max(S)
4. Increase-Key(S, x, k)

``` text
HEAP-MAXIMUM(A)
    return A[1]
```

``` text
HEAP-EXTRACT-MAX(A)
    if A.heap-size < 1
        error "heap underflow"
    max = A[1]
    A[1] = A[A.heap-size]
    A.heap-size = A.heap-size - 1
    MAX-HEAPIFY(A, 1)
    return max
```
The running time of HEAP-EXTRACT-MAX is O(lgn) since it performs only a constant amount of work on top of the O(lgn) time for MAX-HEAPIFY.

``` text
HEAP-INCREASE-KEY(A, i, key):
    if key < A[i]:
        error "new key is smaller than current key"
    A[i] = key
    while i > 1 and A[Parent(i)] < A[i]
        exchange A[i] with A[Parent(i)]
        i = Parent(i)
```

The running time of HEAP-INCREASE-KEY is O(lgn) since the path traced from the node updated in line 3 to the root has length O(lgn).

``` text
MAX-HEAP-INSERT(A, key)
    A.heap-size = A.heap-size + 1
    A[heap-size] = None
    HEAP-INCREASE-KEY(A, A.heap-size, key)
```

The running time of MAX-HEAP-INSERT on an n-element heap is O(lgn).
