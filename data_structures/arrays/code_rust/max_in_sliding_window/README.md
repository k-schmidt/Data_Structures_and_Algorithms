# Find Maximum in Sliding Window

Given a large array of integers and a window of size 'w', find the current maximum in the window as the window slides through the entire array.

## Hints
+ Heap
+ Is it required to store all the elements of current window?

## Solution

Runtime Complexity: O(n)


Memory Complexity: O(w) where 'w' is the window size.


A simple solution to this problem would be to find maximum by scanning all elements within the window *w* every time it slides right. This approach has complexity O(nw).


A slightly better solution is to use a Heap of window size **w**. It will help us find the max quickly. One thing to note is that every time the window moves; we will need to delete one of the existing elements from the heap that is not in the window anymore, and we will need to add a new element.
Both of these operations are O(logw) operations.
The total runtime complexity for this approach will be O(nlog(w)).
Let's challenge ourselves to see if we can come up with a better runtime.


We can reduce the complexity of the previous solution by using a doubly linked list (or a vector) where we can insert/delete at both ends.

### Pseudocode

+ Window size is **w** and array size is n.
+ Iterate the first **w** elements of the array; and for each element in the array, do the following:
    + remove elements from the tail of window(list) that are smaller than or equal to the current element.
+ Push current element at the tail of window.
    + This ensures that the maximum of first **w** elements is at the head of linked list and it can be printed.
+ Run through remaining elements of the array and for each element do the following:
    + Remove all elements from the tail of window that are smaller than or equal to the current element.
    + Remove the element at head if its index no longer falls in current window.
    + Push the current element at the tail of window.
    + Current max is at head and can be printed

### Implementation

``` python
from collections import deque

def find_max_sliding_window(arr, window_size):
    if window_size > len(arr):
        return

    window = deque()

    # find out max for first window
    for i in range(window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)

    print(arr[window[0]])

    for i in range(window_size, len(arr)):
        # remove all numbers that are smaller than current number
        # from the tail of list
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        # remove first number if it doesn't fall in the window
        if window and (window[0] <= i - window_size):
            window.popleft()

        window.append(i)
        print arr[window[0]]
```
