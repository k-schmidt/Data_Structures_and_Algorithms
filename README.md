# Algorithms and Data Structures Study

## What to Know

+ [**Data Structures**](./data_structures/README.md)
    + [Linked List](./data_structures/linked_lists)
    + [Binary Search Tree](./data_structures/binary_search_tree/README.md)
    + Tries
    + Graphs
    + [Stacks](./data_structures/stack/README.md)
    + Queues
    + [Heaps](./data_structures/heap/README.md)
    + [Vectors / ArrayLists](./data_structures/arrays)
    + [Hash Tables](./data_structures/hash_tables/README.md)
+ **Algorithms**
    + Breadth-First Search
    + Depth-First Search
    + [Binary Search](./data_structures/arrays/code_rust/binary_search/README.md)
    + [Merge Sort](./algorithms/merge_sort/README.md)
    + Quick Sort
+ **Concepts**
    + [Bit Manipulation](./concepts/bitwise_operators/README.md)
    + Memory (Stack vs. Heap)
    + [Recursion](./concepts/recursion/README.md)
    + Dynamic Programming
    + [Big O Time and Space](./big_o/README.md)
    + [Object Oriented Design](./concepts/object_oriented_design/README.md)
+ **Math**
    + [Counting Principle, Permutations and Combinations](./math/counting_principle_permutations_combinations/README.md)
    + [Palindrome](./math/palindrome/README.md)
    + [Subsets of a set](./subsets/README.md)
    + [Probability](./math/probability.README.md)
    + [Sum of first N natural numbers](./math/sum_first_n_natural_numbers/README.md)
    + [Slope of a line and derivative](./math/slope/README.md)
    + [Distance Formula](./math/distance_formula/README.md)
    + [Prime Numbers](./math/prime_numbers)
    + [Pigeonhole Principle](./math/pigeonhole_principle/README.md)
    + [LCM and GCD](./math/lcm_and_gcd/README.md)
    + [Inclusion Exclusion Principle](./math/inclusion_exclusion_principle/README.md)
    + [Decimal and Binary](./math/decimal_and_binary/README.md)
    + [Hexadecimal](./math/hexadecimal/README.md)
    + [Solving a quadratic equation](./math/solve_quadratic_equations_using_quadratic_formula/README.md)
    + [Mean, Median, and Mode](./math/mean_median_and_mode/README.md)

## Sorting

### Criteria to Consider

+ How much data is to be sorted?
  + For small data sets it doesn't matter which algorithm you choose because there is little difference in the execution times.
    + Although Mergesort can be implement
+ Does the data fit into memory?
  + If the data set is too large for memory, you may need to split it into smaller chunks for sorting and then combine those sorted chunks to create a the final sorted data set.
+ Is the data already mostly sorted?
  + Adding new data to a sorted list can be done efficiently with certain algorithms, but those same algorithms have poor performance on randomly ordered data.
  + For partially ordered arrays we may not need Nlog(N) compares.
  + For duplicate keys we may not need Nlog(N) compares.
+ How much additional memory does the algorithm require?
  + An *in-place* sorting algorithm sorts the data without using any additional memory.
+ Is relative order preserved?
  + A *stable* sorting algorithm preserves the relative order of data elements that are otherwise identical for sorting purposes.
  + Stability is generally a desirable feature, but in many cases it may be worth sacrificing stability for improved performance.
    + **Stable Sorting Algorithms**
      + Insertion Sort
      + Mergesort
    + **Unstable Sorting Algorithms**
      + Selection Sort
      + Quicksort


Applications have diverse attributes.


+ Stable?
+ Parallel?
+ Deterministic?
+ Keys all distinct?
+ Multiple key types?
+ Linked list or arrays?
+ Large or small items?
+ Is your array randomly ordered?
+ Need guaranteed performance?

![Sorting Summary](./algorithms/sorting_summary.png)

### Selection Sort

+ In iteration `i`, find index `min` of smallest remaining entry.
+ Swap `a[i]` and `a[min]`


1. Find the smallest
2. Swap `a[i]` and `a[min]`
3. Increment `i`


Selection sort **does not care** if the array is partially sorted.

### Insertion Sort

+ In iteration `i`, swap `a[i]` with each larger entry to its left.
+ Increment `i`


**Does depend on the initial order of the data**


Best Case: If the array is in ascending order, insertion sort makes `N-1` compares and 0 exchanges. If the array is partially sorted, insertion sort runs in linear time.


Worst Case: If the array is in descending order (and no duplicates), insertion sort makes ~ `(N^2)/2` compares and ~ `(N^2)/2` exchanges.

### Mergesort

+ Divide array into two halves.
+ Recursively sort each half.
+ Merge two halves.
  + Given two sorted subarrays, take two pointers to the two subarrays, compare their values, and take the min. Increment the pointer pointing to the min that was just taken.


Mergesort uses at most `Nlog(N)` compares and `6Nlog(N)` array accesses to sort any array of size `N`.


Mergesort uses extra space proportional to `N`. The array needs to be of size `N` for the last merge.


We **can** use **Insertion Sort** for small subarray. Mergesort has too much overhead for tiny subarrays. Cutoff to insertion sort for ~ 7 items.


We **can** stop if the the array is aleady sorted. Is the biggest itemin the first half <= smallest item in second half? This helps for partially-sorted arrays.

### Quicksort

1. Randomly shuffle the array
2. Partition so that, for some `j`
   + entry `a[j]` is in place
   + no larger entry to the left of `j`
   + no smaller entry to the right of `j`
3. Sort each piece recursively

#### Partitioning
1. Repeat until `i` and `j` pointers cross
   + Scan `i` from left to right so long as (`a[i] < a[lo]`)
   + Scan `j` from right to left so long as (`a[j] > a[lo]`)
   + Exchange `a[i]` with `a[j]`
2. When pointers cross, exchange `a[lo]` with `a[j]`

#### Implementation Details
1. Partitioning in-place.
   + Using an extra array makes partitioning easier (and stable) but is not worth the cost.
2. Terminating the loop
   + Testing whether the pointers cross is a bit trickier than it might seem.
3. Staying in bounds
   + The `(j == lo)` test is redundant because the iteration will stop when it hits the partitioning element but the `(i == hi)` test is not.
4. Preserving Randomness
   + Shuffling is needed for performance guarantee.
5. Equal Keys
   + When duplicates are present, it is (counter-intuitively) better to stop on keys equal to the partitioning item's key.


Best case: `Nlog(N)`


Worst case: `(N^2)/2` if the random shuffle puts the items exactly in order. Or if all items equal to the partitioning item are on one side (duplicates)


Random shuffle provides a probabilistic guarantee against worst case.


Quicksort **can** run in quadratic time if there are a number of duplicates and the implementation is not done just right.


#### Properties
1. Quicksort is an in-place sorting algorithm
   + Partitioning: constant extra space.
   + Depth of recursion: logarithmic extra space (with high probability).
2. Quicksort is **not** stable
   + Partitioning does a long range exchange.

#### Practical Improvements
1. Even quicksort has too much overhead for tiny subarrays.
2. Cutoff to insertion sort for ~ 10 items.
3. Note: could delay insertion sort until one pass at end.


1. Median of Sample
   + Best choice of pivot item ~ median
   + Estimate true median by taking median of sample
   + Median-of-3 (random) items.

#### Beating Duplication
3-way partitioning


1. Partition array into 3 parts so that:
   + Entries between `lt` and `gt` equal to partition item `v`. Middle partition
   + No larger entries to left of `lt`. Lower partition
   + No smaller entries to right of `gt`. Greater partition


Implementation:


1. Let `v` be partitioning item `a[lo]`
2. Scan `i` from left to right
   + `(a[i] < v)`: exchange `a[lt]` with `a[i]`; increment both `lt` and `i`
   + `(a[i] > v)`: exchange `a[gt]` with `a[gt]`; decrement `gt`
   + `(a[i] == v)`: increment `i`

### Priority Queues

Remove (find) the largest (or smallest) item.


Typical constraint is that there is not enough memory to store **N** items

#### Priority Queue API

1. MaxPQ()
   + Create an empty priority queue
2. insert(value)
   + Insert a key into the priority queue
3. delMax()
   + Return and remove the largest key
4. isEmpty()
   + is the priority queue empty?

#### Find the largest M Items in a Stream of N Items

``` java
// Use a min priority queue
MinPQ<Transaction> pq = new MinPQ<Transaction>();

while (STdIn.hasNextLine())
{
    String line = StdIn.readLine();
    Transaction item = new Transaction(line);
    pq.insert(item);
    if (pq.size() > M)  // pq contains largest M items
        pq.delMin();
}
```


1. Sorting the N items would take `NlogN` time and `N` space
2. Using an **elementary priority queue** takes `MN` time and `M` space
3. **Best in practice** is to use a **Binary Heap** which would take `NlogM` time and `M` space
4. Best in theory is `N` time and `M` space

### Binary Heaps

Implements all operations of priority queues efficiently.


1. Binary Tree
   + Empty or Node with links to left and right Binary trees
2. Complete Tree
   + Perfectly balanced, except for bottom level
   + **Property**
     + Height of complete tree with `N` nodes is `logN`
       + Height only increases when `N` is a power of 2.

#### Binary Heap Representations

##### Heap-ordered binary tree
1. Keys in nodes.
2. Parent's key no smaller than children's key

##### Array Representation
1. Indices start at 1
2. Take nodes in level order
3. No explicit links needed

#### Binary Heap Properties

1. Largest key is `a[1]` which is root of binary tree
2. Can use array indices to move through tree.
   + Parent of node at `k` is at `k/2`
   + Children of node at `k` are at `2k` and `2k+1`

#### Promotion in a Heap

##### Child's key becomes larger than it's parent's key

1. Exchange the key in child with the key in parent.
2. Repeat until heap order is restored.

#### Demotion in a Heap

##### Parent's key becomes smaller than one (or both) of its children

1. Exchange key in parent with key in larger child.
2. Repeat until heap order is restored.

#### Delete the maximum in a heap

1. Exchange root with node at the end and pop it off the heap.
2. Demote the node until heap order is restored.


**Cost**: At most `2logN` compares.

#### Binary Heap Considerations

1. Immutability of keys
2. Underflow and Overflow
   + Throw exception if deleting from empty Priority Queue
   + Throw exception if adding to a max-out Priority Queue
3. Minimum-oriented priority queue
   + Replace `less()` with `greater()`
   + Implement `greater()`
4. How would you implement remove an arbitrary item?
5. How would you implement change the priority of an item?

### Heapsort

1. Create Max-Heap with all N keys
2. Repeatedly remove the maximum key using the Delete Maximum in a heap method defined two sections ago.

#### Heap Construction
Build heap using bottom-up method

``` java
for (int k = N/2; k >= 1; k--)
    sink(a, k, N);
```

#### Sortdown
1. Remove the maximum, one at a time.
2. Leave in array, instead of nulling out.

``` java
while (N > 1)
{
    exch(a, 1, N--);
    sink(a, 1, N);
}
```

#### Mathematical Analysis
+ Heap construction uses `<= 2N` compares and exchanges.
+ Heapsort uses `<= 2NlogN` compares and exchanges.


This is significant because it is an **in-place** algorithm with `NlogN` worst-case.


+ **Mergesort**: required linear extra space
+ **Quicksort**: quadratic time in the worst case


Heapsort is optimal for both time and space but:


+ Inner loop is longer than quicksort's
+ Makes poor use of cache memory
  + Has no local memory reference
+ Not stable.
