# Chapter 3

## Seven Functions Used in This Book

1. Constant Function
2. Logarithm Function
    3. `x = logb(n) iff b^x = n`
    4. Logarithm Rules
        5. `logb(ac) = logb(a) + logb(c)`
        6. `logb(a/c) = logb(a) - logb(c)`
        7. `logb(a^c) = clogb(a)`
        8. `b^logd(a) = a^logd(b)`
9. Linear Function
10. N-Log-N Function
11. Quadratic Function
    12. Summation of Series
        13. `n(n+1)/2`
14. Cubic Function
    15. Using a summation, we can rewrite our summation formula as the sum from `i=1 to n, i = n(n+1)/2`.
    16. Likewise, we can rewrite a polynomial f(n) of degree d with coefficients a0, ..., ad as `f(n) = the sum from i=0 to d, ain^i`.
17. Exponential Function
    18. Exponent Rules
        19. `(b^a)^c = b^(ac)`
        20. `b^ab^c = b^(a+c)`
        21. `b^a/b^c = b^(a-c)`


Geometric Sums: For any integer n>=0 and any real number a such that a > 0 and a !=1, consider the summation:

```
The sum from i=0 to n, a^i = 1 + a + a^2 + ... + a^n

Remembering that a^0=1 if a > 0.

This summation is equal to:

(a^(n+1) - 1)/(a-1)
```

### Examples
3.10: `5n^2 + 3nlog(n) + 2n + 5 is O(n^2)


Justification: `5n^2 + 3nlog(n) + 2n + 5 <= (5 + 3 + 2 + 5)n^2 = cn^2 for c = 15, when n >= n0 = 1`
