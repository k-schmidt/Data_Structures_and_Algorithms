# Sum of Two Values

Given an array of integers and a value, determine if there are any two integers in the array which sum equal to the given value.

## Hints
- Hashable
- Sort array

## Solution #1
Runtime Complexity - O(n)


Memory Complexity - O(n)

### Pseudocode

1. Scan whole array once and store visited elements in a hash set.
2. During scan, for every element 'e' in array, we check if 'val' - 'e' is present in the hash set i.e. 'val' - 'e' is already visited.
    3. If 'val' - 'e' is found in the hash set, it means there is a pair (e, val - e) in array whose sum is equal to the given val.
    4. If we have exhausted all elements in the array and didn't find any such pair, function with return false.

### Implementation

``` python
def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return True

        found_values.add(a)

    return False
```

## Solution #2
Runtime Complexity - O(nlogn) required to sort the array, otherwise O(n)


Memory Complexity - O(1)

### Pseudocode

``` text
// assume 0 is the first index in array
// and n is the total number of elements in array
left = 0
right = n-1
while left is less than right
    sum = array[left] + array[right]
    if sum == val return True
    if sum is less than val
        // sum is smaller than value
        // means pair can only exist to the
        // right of left element, so left element
        // should be moved one step next
        left = left + 1
    else
        // sum is greater than value
        // means pair can only exist to the
        // left of right element, so right element
        // should be moved one step previous
        right = right - 1
```

### Implementation

``` python
# This solution only works if the array is sorted
# Does not require any extra memory

def find_sum_of_two_2(A, val):
    i = 0
    j = len(A) - 1
    while i < j:
        s = A[i] + A[j]
        if s == val:
            return True

        if s < val:
            i+=1
        else:
            j-=1

    return False
```
