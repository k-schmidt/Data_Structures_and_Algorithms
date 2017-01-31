# Implement Quicksort

Given an integer array, sort it in ascending order using quicksort.

## Hints
+ Divide and Conquer

## Solution
Runtime Complexity - O(nlogn)


Memory Complexity - O(logn)


Recursive solution has O(logn) memory complexity as it will consume memory on the stack.

### Psuedocode

1. Select a pivot element from the array. We can pick the first element as the pivot (following Hoare's algorithm). Another common approach is to select a random element as the pivot.
2. Reorder the array by comparing with the pivot element such that smaller values end up at the left side, and the larger values and up at the right side of the pivot.
3. Now, the pivot element is in its correct sorted position.

### Implementation

``` python
# Below partition is using Hoare's algorithm
def partition(arr, low, high):
    pivot_value = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot_value and i <= high:
            i += 1
        while arr[j] > pivot_value:
            j -= 1
        if i < j:
            # swap arr[i], arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low] = arr[j]
    arr[j] = pivot_value

    return j

def quick_sort_rec(a, l, h):
    if h > l:
        pivot_index = partition(a, l, h)
        quick_sort_rec(a, 1, pivot_index - 1)
        quick_sort_rec(a, pivot_index + 1, h)

def quick_sort(a):
    quick_sort_rec(a, 0, len(a)-1)
```
