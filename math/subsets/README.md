# Subsets and Proper Subsets

## Example

``` python
A = {a, b, c, d}
B = {a, c, d}
C = {d, c, b, a}
```

Since all of B's elements are also in A, then B is a subset of A.
A is the **superset** of B.
All of the elements in set C are also found in set A, then C is a subset of A.
Since C and A are equal to eachother, then A can also be a subset of C.
Set B is a **proper subset** of A since A has less elements than set A.

## Further Example
How many subsets can a set have?

``` python
A = {a}
B = {a, b}
C = {a, b, c}
```

For each element of a set, it will either be in the subset or it will not.
Therefore, the equation is `2^n` where n is the number of elements in the set.
n is the **cardinality** of the set.
