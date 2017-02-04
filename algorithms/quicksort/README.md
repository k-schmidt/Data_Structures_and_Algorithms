# Quicksort

Quicksort, like merge sort, applies teh divide-and-conquer paradigm.


Three step divide-and-conquer process for sorting a typical subarray.


1. Divide
  + Partition the array into two (possibly empty) subarrays such that each element is less than or equal to A[q], which is, in turn, less than or equal to each element of the bottom half of A is less than or equal to each element of the top half. Return and compute the index of the midpoint.
2. Conquer
  + Sort the two subarrays by recursive calls to quicksort.
3. Combine
  + Because the subarrays are already sorted, no work is needed to combine them: the entire array is now sorted.

``` text
QUICKSORT(A, p, r)
    if p < r
        q = Partition(A, p, r)
        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)

PARTITION(A, p, r)
    x = A[r]
    i = p - 1
    for j = p to r - 1
        if A[j] <= x
            i += 1
            exchange A[i] with A[j]
    exchange A[i+1] with A[r]
    return i + 1
```

## Performance of Quicksort

The running time of quicksort depends on whether the partitioning is balanced or unbalanced, which depends on which elements are used for partitioning.
If the partitioning is balanced, the algorithm runs asymptotically as fast as merge sort.
If the partitioning is unbalanced, it can run asymptotically as slowly as insertion sort.

### Worst-case partitioning


``` text
T(n) = T(n - 1) + T(0) + Omega(n)
T(n) = T(n - 1) + Omega(n)
```

We can use the substitution method to prove `T(n) = Omega(n^2)`

### Best-case partitioning

If there is an even split:

``` text
T(n) = 2T(n/2) + Omega(n)
```

By case two of the master theorem, this recurrence has the solution `T(n) = Omega(nlogn)`

### Balance partitioning

Every level of the tree has cost cn, until the recursion reaches a boundary condition at depth Omega(logn), and then the levels have cost at most cn. The total cost of quicksort is therefore O(nlogn).
The running time is O(nlogn) whenever the split has constant proportionality.
