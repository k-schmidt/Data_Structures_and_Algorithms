# Rotate Array

Given an array of integers, rotate the array by 'N' elements.

## Hints

+ Reverse

## Solution #1

Runtime Complexity - O(n)


Memory Complexity - O(1)

### Pseudocode

+ Reverse the elements of the original array.
+ Reverse the elements from o -> N-1
+ Reverse the elements from N -> Length-1

### Implementation

``` python
def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotate_array_in_place(arr, n):
    length_arr = len(arr)

    # Normalize rotations
    # if n > array size or n is negative
    n = n % length_arr
    if n < 0:
        n += length_arr

    reverse_array(arr, 0, length_arr - 1)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, n, length_arr - 1)
```

## Solution #2

Runtime Complexity - O(n)


Memory Complexity - O(n)

### Pseudocode

+ Store the last 'N' elements into a temporary array.
+ Shift the original array towards right by 'L-N' places. Here, L is the length of the array.
+ Copy the temporary array at the beginning of the original array.

### Implementation

``` python
def rotate_array(arr, n):
    length_arr = len(arr)

    # Let's normalize rotations
    # if n > array size or n is negative
    n = n % length_arr
    if n < 0:
        n+=length_arr

    temp = []
    for i in range(n):
        temp.append(0)

    # Copy last N elements of array into temp
    for i in range(n):
        temp[i] = arr[length_arr - n + i]

    # Shift original array
    for i in range(length_arr-1, n-1, -1):
        arr[i] = arr[i-n]

    # Copy temp into original array
    for i in range(n):
        arr[i] = temp[i]
```
