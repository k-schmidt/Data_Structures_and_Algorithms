# Dynamic Programming

## Dynamic Programming 1: Fibonacci, Shortest Paths

It is especially good for optimization problems i.e. shortest paths.
Minimize/Maximize problems.
Kind of exhaustive search which can lead to exponential time without Dynamic Programming (DP) but if you solve it with DP it can lead to polynomial time.


DP is often called "careful brute force"


General way to solve DP is to split the problem into subproblems and re-use.


DP is made up of memoization, recursion, and guessing.

### Compute Fibonacci Numbers

``` python
F1 = F2 = 1
Fn = Fn-1 + Fn-2
```

#### Goal: Compute the Fn Fibonacci number.


``` python
# Start with naive recursive algorithm.
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# But this is EXPONENTIAL TIME
T(n) = T(n-1) + T(n-2) + O(1)  # Recurrence
```

### Memoized DP Algorithm

``` python
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f
```

Whenever we compute a fibonacci number we add it to the dictionary. If we have already solved that fibonacci problem then return the answer otherwise compute it. fib(k) only recurses the first time it is called for every k.
The memoized calls cost O(1). The number of non-memoized calls is n. The nonrecursive work per call is O(1), therefore the total time is O(n).


In general, in DP:
1. memoize (remember) solutions to **subproblems**
2. re-use solutions to **subproblems** that help solve the problem.


Need to identify what the **subproblems** are.


time = # subproblems * time/subproblems O(1) (don't count recursions - we get those for free)


### Bottom-up DP Algorithm

``` python
fib = {}
for k in range(1, n+1):
    if k <=2:
        f = 1
    else:
        f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]
```

In general, the bottom-up computation does exactly the same computation. Topological sort of subproblem dependency DAG.


We can often save space because we only need to keep track of the last computed value.

### Shortest Paths

Guessing: don't know the answer? Guess. **Try all guesses.** And take the best one.


Infinite time for DAGs: O(V + E) time for subproblem delta(s, v) = indegree(v) + 1


total time = sum of indegree(v) = O(E + V)


**subproblem dependencies should be acyclic.**


If you are acyclic then the running time is **time = #subproblems * (time/subproblem = O(1))


Need to take a clycic graph and make it acyclic.
