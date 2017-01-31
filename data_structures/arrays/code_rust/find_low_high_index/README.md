# Find low/high Index

Given a sorted array of integers, return the low and high index of the given key. Return -1 if not found.
The array length can be in millions with lots of duplicates.

## Hints
- Binary Search

## Solution 1
Runtime Complexity - Since we are using binary search the runtime complexity is O(logn). Although we use binary search twice the asymptotic complexity is still O(logn).


Memory Complexity - O(1)

### Pseudocode
Algorithm for finding the low index:


1. At every step, consider the array between low and high indices.
2. Calculate the mid index.
3. If element at mid index is less than the key, low becomes mid + 1 (to move towards start of range)
4. If element at mid is greater or equal to the key, high becomes mid - 1. Index at low remains the same.
5. When low is greater than high, low would be pointing to the first occurrence of the key.
6. If element at low does not match the key, return -1.


We can find the high index by slightly modifying the above condition to switch **low** index to **mid+1** when element at mid index is **less** than equal to the **key** and to switch the **high** index to **mid-1** when element at mid is **greater** than the **key**.

### Implementation

``` python
def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:
        mid_elem = arr[mid]

        if mid_elem < key:
            low = mid+1
        else:
            high = mid-1

        mid = low + (high - low)/2

    if arr[low] == key:
        return low

    return -1

def find_high_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:
        mid_elem = arr[mid]

        if mid_elem <= key:
            low = mid+1
        else:
            high = mid-1

        mid = low + (high-low)/2


    if arr[high] == key:
        return high

    return -1
```
