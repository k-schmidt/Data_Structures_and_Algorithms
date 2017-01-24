# Asymtotic Notation

For small input sizes, O(n^2) runs faster than O(n) but as the input size gets larger O(n^2) will run slower than O(n)


Binary Search - O(log(n))


Best case is measured in Omega
Binary search best case is Omega(1), when you get lucky and choose the element you are looking for.


Theta - best and worse cases are the same


``` python
st = "Your Name"
l = len(st)  # 9

# Omega(1)
# O(1)
"""
Since Omega and Big O are the same runtimes then we can say this problem has:
Theta(1) compelexity
```


When we compute Big O notation, we drop the constants as well as all other elements of a Big O equation that are less than the asymtotically largest element. Furthermore, we drop all coeffecients. Only the asymtotically largest element of the derived Big O equation influences the run-time of the program.

## O(1)

``` python
arr = [1, 2, 3, 4]
arr[0] = "Your name"  # Order of 1 operation
```

## O(n)

``` python
is_found = False
value = 4
arr = [1, 2, 3, 4]
for item in arr:
    if item == value:
        is_found = True
print(is_found)
```

## O(n^2)

``` python
# Bubble Sort


def bubble_sort():
    arr = [1, 2, 3, 4, 5]
    index1 = len(arr) - 1
    index2 = 0
    while index1 > 1:
        while index2 < index1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            index2 += 1
        index1 -= 1
    return arr
```

## O(log(n))
Decreases by roughly 50%. Log(n) algorithms are very efficient.

``` python
# Binary Search


def bin_search(value, arr):
    low_index = 0
    high_index = len(arr) - 1
    while low_index <= high_index:
        middle_index = (high_index + low_index) // 2
        if arr[middle_index] < value:
            low_index = middle_index + 1
        elif arr[middle_index] > value:
            high_index = middle_index - 1
        else:
            return middle_index
            low_index += 1
    return "Not Found"
```

## O(nlog(n))
Comparisons = log n!
Comparisons = log(n) + log(n-1) + log(n-2) + ... + log(1)
Comparisons = nlog(n)

``` python
## Quicksort


def partition_arry(left, right, pivot, arr):
    left_pointer = left - 1
    right_pointer = right
    while True:
        while arr[left_pointer] < pivot:
            left_pointer += 1

        while right_pointer > 0 and arr[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        else:
            temp = arr[left_pointer]
            arr[left_pointer] = arr[right_pointer]
            arr[right_pointer] = temp
    temp = arr[left_pointer]
    arr[left_pointer] = arr[right]
    arr[right] = temp
    return left_pointer


def quick_sort(left, right, arr):
    if (left - right) <= 0:
        return
    else:
        pivot = arr[right]
        pivot_location = partition_array(left, right, pivot, arr)
        quick_sort(left, pivot_location - 1)
        quick_sort(pivot_location + 1, right)
```

## Mathematical Explanation
f(n) is O(g(n)) if c and n0 f(n) <= cg(n) for all n > n0. (Worst Case)


f(n) = 4n^2 + 16n + 2


is f(n) => O(n^4)


4n^2 + 16n + 2 < n^4


n = 0, 2 < 0 False


n = 1, 22 < 1 False


n = 2, 50 < 16 False


n = 3, 86 < 81 False


n = 4, 130 < 256 True


f(n) is Omega(g(n)) if c and n0 iff f(n) >= cg(n) for all n > n0. (Best Case)


f(n) = 4n^2 + 16n + 2


is f(n) => Omega(n^2)


4n^2 + 16n + 2 > n^2 True


is f(n) => Omeaga(n^3)


4n^2 + 16n + 2 > cn^3 False


4n^2 is the dominating term. Whatever the constant is, it won't matter because n^2 and n^3 are the dominating terms and have a greater influence on the asymtotic complexity.


f(n) is Theta(g(n)) iff


1. f(n) is O(g(n))
2. f(n) is Omega(g(n))


f(n) = 4n^2 + 16n + 2


is f(n) => Theta(n^2)


f(n) is Omega(n^2)?


c = 1, n0 = 0


4n^2 + 16n + 1 > n^2 True


f(n) is O(n^2)?


4n^2 + 16n + 1 < n^2 True


f(n) is Theta(g(n)) because the equation is both O(n^2) and Omega(n^2)


When we describe the asymtotic complexity of an algorithm, we choose the tightest bound there is to describe it. O(n^3), O(n^4), O(n^5) etc all satisfy our theorem but we choose the smallest power to describe the smallest worst case complexity. To know that you've chosent the tightest bound, you should also test Omega(n), and hence Theta(n).


## O(log(n))
logx(n) => O(logy(n)) where x and y are the values of how much the original data structure is reduced by.


1. y = x, c = 1, n = 0, True
2. y > x
    + log2(n) is O(log8(n))
    + log2(n) <= 3log8(n) == log8(n)^3 True
    + c = log2(8) = 3


T(n) = logx(n), then T(n) is O(logx(n)). We have the flexibility to determine the base (x) of the logarithm.

T(n) = O(log(n))
