"""
Given a large array of integers and a window of size w, find current maximum in the window as the window slides through the entire array.

Hints:
+ Heap
+ Is it required to store all the elements of current window?
"""
from collections import deque


def max_in_window_of_array(w, arr):
    if w > len(arr):
        raise Exception("Window is larger than array")

    window = deque()

    for i in range(w):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)

    print(arr[window[0]])

    for i in range(w, len(arr)):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        if window and (window[0] <= i - w):
            window.popleft()

        window.append(i)
        print(arr[window[0]])
