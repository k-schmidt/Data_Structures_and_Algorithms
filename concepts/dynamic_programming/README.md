## Dynamic Programming (Memoization)

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
