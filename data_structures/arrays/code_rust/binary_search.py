"""
Binary Search
Given a sorted array of integers, return the index of the given key. Return -1 if not found.

Hints:
Divide and conquer
"""
arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188,
       199, 200, 210, 222]


def binary_search_recur(arr, search_num, low, high):
    if low > high:
        return -1
    mid = low + ((high - low) // 2)
    if arr[mid] == search_num:
        return mid
    elif arr[mid] > search_num:
        return binary_search_recur(arr, search_num, low, mid - 1)
    else:
        return binary_search_recur(arr, search_num, mid + 1, high)


def binary_search(arr, key):
    """
    O(logn) Runtime Complexity
    O(logn) Memory Comlexity
    """
    return binary_search_recur(arr, key, 0, len(arr) - 1)


def binary_search_iter(arr, search_num):
    """
    O(logn) Runtime Complexity
    O(1) Memory Complexity
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == search_num:
            return mid
        elif arr[mid] > search_num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    print(binary_search(arr, 75))
    arr = [1, 10, 20, 47, 59, 63, 75, 88, 99]
    print(binary_search_iter(arr, 70))
