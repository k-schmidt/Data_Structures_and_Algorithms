# Search Rotated Array

Search a given number in a sorted array that has been rotated by some arbitrary number.

## Hints

+ Linear search is not an acceptable solution
+ Think modified binary search

## Solution

Runtime Complexity: O(logn)


Space Complexity: O(logn)


The solution is essentially binary search with some modifications. If we look at the array, we notice that at least one half of the array is always sorted.
We can use this property to our advantage. If the number n lies within the sorted half of the array then our problem is basic binary search.
Otherwise descard the sorted half and keep examining the unsorted part.
Since we are partitioning array in half at each step this give us O(logn) runtime complexity.

### Implementation

``` python
def binary_search(arr, st, end, key):

    # assuming all the keys are unique

    if st > end:
        return -1

    mid = st + (end - st) / 2

    if arr[mid] == key:
        return mid

    if (arr[st] < arr[mid] and key < arr[mid] and key >= arr[st]):
        return binary_search(arr, st, mid-1, key)
    elif (arr[mid] < arr[end] and key > arr[mid] and key <= arr[end]):
        return binary_search(arr, mid+1, end, key)
    elif arr[st] > arr[mid]:
        return binary_search(arr, st, mid-1, key)
    elif arr[end] < arr[mid]:
        return binary_search(arr, mid+1, end, key)

    return -1

def binary_search_rotated(arr, key):
    return binary_search(arr, 0, len(arr)-1, key)
```
