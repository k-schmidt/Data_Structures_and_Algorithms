# Binary Search

Given an array of integers, return the index of the given key. Return -1 if not found

## Hints

Divide and Conquer

## Solution 1

Runtime Complexity: O(logn)


Memory Complexity: O(logn)


Recursive solution has O(logn) memory complexity as it will consume memory on the stack.
Binary search is used to find the index of an element in a sorted array.
If the element doesn't exist, that can be determined efficiently as well.
The algorithm divides the input array by half at every step.
After every step, either we have found the index that we are looking for or half of the array can be discarded. Hence, solution can be calculated in O(logn) time.

### Pseudocode

1. At every step, consider the array between **low** and **high** indices.
2. Calculate the **mid** index.
3. If the element at the **mid** index is the key, return **mid**.
4. If the element at **mid** is greater than the key, then reduce the array size such that **high** becomes **mid-1**. Index at **low** remains the same.
5. If element at **mid** is less than the key, then reduce the array size such that **low** becomes **mid+1**. Index at **high** remains the same.
6. When **low** is greater than **high**, key doesn't exist. Return -1.

### Implementation

``` python
def binary_search_rec(a, key, low, high):
    if low > high:
        return -1

    mid = low + ((high - low) / 2)
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search_rec(a, key, low, mid-1)
    else:
        return binary_search_rec(a, key, mid+1, high)

def binary_search(a, key):
    return binary_search_rec(a, key, 0, len(a) - 1)
```

## Solution 2

Runtime Complexity: O(logn)


Memory Complexity: O(1)

### Implementation

``` python
def binary_search_iterative(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = low + ((high - low) / 2)

        if a[mid] == key:
            return mid

        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```
