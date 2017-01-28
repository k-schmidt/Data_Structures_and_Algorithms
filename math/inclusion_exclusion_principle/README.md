# Inclusion/Exclusion Principle

Is a way to avoid overcounting.

## Two Circles
If you have a venn diagram with two circles, try to count everything included in the venn diagram only once.
The middle, overlapping data is typically counted twice.


A + B - (A and B)


## Three Circles
Now suppose you have a venn diagram with three circles.
You will be counting 3 sections twice and 1 section 3 times.


Suppose we subtract each of the 3 intersections we are counting twice:


A + B + C - (A and B) - (A and C) - (B and C)


But this introduces a new problem: we are not counting the middle section at **all**.
So lets add it back:


A + B + C - (A and B) - (A and C) - (B and C) + (A and B and C)


## Principle
Now you should notice a pattern.
1. Add the entire objects
    2. If one or more objects
2. Subtract all the cases of overlapping objects.
    3. If two or more objects
3. Add the overlap of all objects
    4. If three of more objects


The signs switch back and forth depending on the number of objects.

## Four Objects

1. Add one object at a time


`A + B + C + D`


2. Subtract overlap of two objects
    3. Notice that this is the same as 4 choose 2 = 6


`- (A and B) - (A and C) - (A and D) - (B and C) - (B and D) - (C and D)`


3. Add the intersections of 3 objects


`+ (A and B and C) + (A and B and D) + (B + D + C) + (A and C and D)`


4. Subtract the overlap of four objects


`- (A and B and C and D)`


(4 choose 1) - (4 choose 2) + (4 choose 3) - (4 choose 4)


**Binomial Theorem** - describes the algebraic expansion of powers of a binomial.


(n!) / ((n - k)! * k!)
