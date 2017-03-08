def partition(arr, low, high):
    pivot_value = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        print(left, right)
        while left <= right and arr[left] <= pivot_value:
            left += 1
        while right >= left and arr[right] >= pivot_value:
            right -= 1
        if right < left:
            done = True
        else:
            arr[right], arr[left] = arr[left], arr[right]
    arr[right], arr[low] = arr[low], arr[right]
    return right


def quick_sort_rec(a, l, h):
    if l < h:
        pivot_index = partition(a, l, h)
        quick_sort_rec(a, l, pivot_index - 1)
        quick_sort_rec(a, pivot_index + 1, h)


def quick_sort(a):
    quick_sort_rec(a, 0, len(a) - 1)


if __name__ == '__main__':
    a = [6, 2, 4, 3, 2, 1]
    quick_sort(a)
    print(a)
