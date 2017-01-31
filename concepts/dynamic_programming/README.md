## Dynamic Programming (Memoization)

## Steps to Solve
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

## Explanation
Take a recursive algorithm and find the overlapping subproblems (the repeated calls).
You then cache those results for future recursive calls.

## Example

``` python
## Compute Fibonacci Numbers Recursively


def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    return fib(i-1) + fib(i - 2)
```


What is the runtime of the above?
Drawing the recursive calls as a tree is a great way to visualize the call stack and calculate the runtime of a recursive algorithm.

## Rod-Cutting Problem
Given a rod of length n inches and a table of prices, pi for i = 1, 2, 3, 4, ..., n, determine the maximum revenue rn obtainable by cutting up the rod and selling the pieces. Note if the price pn for a rod of length n is large enough, an optimal solution may require no cutting at all.
