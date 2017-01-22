# Recursion

## Definition

Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling itself. Each recursive call adds a new layer to the stack. If your algorithm recurses to a depth of n, it uses at least O(n) memory.

## How to Approach
### Bottom-Up Approach
Start with knowing how to solve the problem for the simple case, like a list with only one element.
Then we figure out how to solve the problem for two elements, then for three elements, and so on.
Think about how you can *build* the solution for one case off of the previous case (or multiple previous cases).

### Top-Down Approach
Think about how we can divide the problem for case N into subproblems.
Be careful of overlap between cases.

### Half-and-Half Approach
Often effective to divide the dataset in half.
Binary search, for example, uses a half-and-half approach.
When we look for an element in a sorted array, we first figure out which half of the array contains the value.
Then recurse and search.

## Example

``` python
## Iterative
def list_sum(numlist):
    theSum = 0
    for i in numlist:
        theSum = theSum + i
    return theSum

## Recursive
def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])
```


Each time we make a recursive call we are solving a smaller problem, until we reach the point where the problem cannot get any smaller.


## The Three Laws of Recursion

1. A recursive algorithm must have a **base case**.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.

### Self Check

How many recursive calls are made when computing the sum of the list [2, 4, 6, 8, 10]?
+ 6
+ 5
+ 4
    + Correct
+ 3


Suppose you are going to write a recursive function to calculate the factorial of a number. `fact(n)` returns `n * (n-1) * (n-2) * ...` Where the factorial of zero is defined to be 1. What would be the most appropriate base case?
+ `n == 0`
+ `n == 1`
+ `n >= 0`
+ `n <= 1`
    + Correct
    + This is the most efficient, and even keeps your program from crashing if you try to compute the factorial of a negative number.

## Converting an Integer to a String in Any Base

``` python
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]
```

``` python
## Write a function that takes a string as a parameter and returns a new string
## that is the reverse of the old string


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
```

``` python
## Write a function that takes a string as a parameter and returns True if the string is a palindrome,
## False otherwise


def remove_white(s):
    return [char for char in s if char not in [" ", "'"]]


def is_pal(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])
```

## Stack Frames, Implementing Recursion

Suppose that instead of concatenating the result of the recursive call to `to_str` with the string from `convert_string`, we modified the algorithm to push the strings onto a stack prior to making the recursive call.


``` python
s = Stack()


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            s.push(convert_string[n])
        else:
            s.push(convert_string[n % base])
        n = n // base
    res = ""
    while not s.isEmpty():
        res = res + str(s.pop())
    return res
```


Each time we make a call to `to_str`, we push a character on the stack.
The example gives us some insight into how Python implements a recursive function call.
When a function is called in Python, a **stack frame** is allocated to handle the local variables of the function.
When the function returns, the return value is left on top of the stack for the calling function to access.
