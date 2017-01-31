# Move zeros to left

Given an integer array, move all elements containing '0' to the left while maintaining the order of other elements in the array.

## Hints
- Counting
- Reader/Writer

## Solution
Runtime Complexity - Linear, O(n)


Memory Complexity - Constant, O(1)

### Pseudocode
1. While moving `read_index` towards the start of the array:
    2. If `read_index` points to '0', skip
    3. If `read_index` points to non-zero, write to `write_index` and decrement `write_index`.

### Implementation

``` python
def move_zeros_to_left(A):
    if len(A) < 1:
        return

    lengthA = len(A)
    write_index = lengthA - 1
    read_index = lengthA - 1

    while read_index >= 0:
        if A[read_index] != 0:
            A[write_index] = A[read_index]
            write_index -= 1

        read_index -= 1

    while write_index >= 0:
        A[write_index] = 0
        write_index -= 1
```
