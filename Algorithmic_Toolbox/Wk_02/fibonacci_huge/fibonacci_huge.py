# Uses python3
import sys
from collections import Counter

def lengths(seq):
    base = [0,1]
    for i in range(2, len(seq)):
        if (i + 1) <= len(seq):
            if (seq[i] == base[0] and seq[i+1] == base[1]):
                return len(base)
            else:
                base.append(seq[i])
    return len(base)

def gcd(a, b):
    d = 1
    if a % b == 0:
        return b
    while a % b != 0:
        d = a % b
        a,b = b,d
    return d

def lcm(a, b):
    return (a*b)//gcd(a,b)

def pisano_length(n):
    s = []
    a = 0
    k = 0
    b = 1
    while s[:k] != s[k:] or k < 1:
        s.append(a % n)
        k = len(s) // 2
        a, b = b, a + b
    return k

def pisano_length_coprimes(n):
    p = [2]
    if n == 2:
        return (pisano_length(n), pisano_length(1))
    elif n == 3:
        return (pisano_length(n), pisano_length(1))
    else:
        for i in range(3,n,2):
            if any(i % x == 0 for x in p):
                continue
            elif n % i == 0:
                co = n // i
                if co % i == 0:
                    continue
                else:
                    print(n, i)
                    return (pisano_length(i), pisano_length(n//i))
            else:
                p.append(i)


def fib(n,m):
    fib_a = 0
    fib_b = 1
    base = [0,1]
    pisano = [0,1]
    for i in range(2, n+1):
        fib_max = fib_a + fib_b
        pisano.append(fib_max % m)
        print(pisano)
        print(base)
        print(len(pisano))
        print(i)
        if pisano[i] == base[1] and pisano[i-1] == base[0]:
            return len(base[:i-1])
        else:
            base.append(pisano[i])
        fib_a = fib_b
        fib_b = fib_max

def find_repetition(p):
    lookup = Counter()
    for i in p:
        lookup[i] += 1
    return len([key for key, value in lookup.items() if value == min(lookup.values())])

def get_fibonaccihuge(n, m):
    pisano_length_1, pisano_length_2 = pisano_length_coprimes(m)
    total_pisano_length = lcm(pisano_length_1, pisano_length_2)
    rem = n % total_pisano_length
    return rem % m

"""
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonaccihuge(n, m))
"""
