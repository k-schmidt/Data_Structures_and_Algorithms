# Find the Smallest Commone Number

Given three integer arrays sorted in ascending order, find the smallest number that is common in all three arrays.

## Hints
+ Take advantage of the sorted arry to reduce complexity
+ Use three pointers.

## Solution

Runtime Complexity: O(n)


Memory Complexity: O(1)

### Pseudocode

We will use 3 iterators simultaneously to travers the arrays.
We can start off by traversing the arrays from the 0th index, which will be the smallest value of each array.


If the values of the array indices pointed by the 3 iterators are:
+ Equal: that's the result. We'll just return the value.
+ Otherwise, we'll advance the iterator that's pointing to the smallest number among the three.


If any of the iterators has reached the end of the array while we haven't found the common number, we'll return -1.

### Implementation

``` python
def find_least_common_number(a, b, c):
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):

        if a[i] == b[j] and b[j] == c[k]:
            return a[i]

        # Let's advance the iterator
        # for the smallest value.

        if a[i] <= b[j] and a[i] <= c[k]:
            i+=1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j+=1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k+=1

    return -1
```
