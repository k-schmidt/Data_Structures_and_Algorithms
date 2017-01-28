# Bitwise Operators

Lets say we have two different values

``` python
"""
Binary And
Goes through and puts a zero unless the top and the bottom are both 1's.
"""

a = 50     # 110010
b = 25     # 011001

c = a & b  # 010000

print(c)   # 16 = 010000

"""
Binary Right Shift
Take bits and shift them right
"""

x = 240    # 11110000
y = x >> 2  # shift x two spots to the right -> 00111100 = 60
```
