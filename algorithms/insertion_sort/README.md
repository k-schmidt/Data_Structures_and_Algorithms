# Insertion Sort
Begin with an empty array and as you choose random digits you place the digits in its proper position from right to left.

``` text
# In-place
INSERTION-SORT(A)
for j = 2 to A.length:
    key = A[j]
    // Insert A[j] into the sorted sequence A[1..j-1].
    i = j - 1
    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
```

``` python
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
```

## Loop Invariants
At the start of each iteration of the **for** loop, the subarray A[1..j-1] consists of the elements originally in A[1..j-1], but in sorted order.


We must show three things about a loop invariant:
1. **Initialization**: It is true prior to the first iteration of the loop.
2. **Maintenance**: If it is true before an iteration of the loop, it remains true before the next iteration.
3. **Termination**: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct.
