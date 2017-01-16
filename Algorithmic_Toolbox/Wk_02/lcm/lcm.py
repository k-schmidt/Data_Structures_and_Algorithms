# Uses python3
import random


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

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
    """
    while True:
        a = random.randint(1, 2000000000)
        b = random.randint(1, 2000000000)
        l = lcm(a,b)
        g = gcd(a, b)
        m = (a * b)
        if l * g == m or g == 1:
            print("OK")
        else:
            print("{}, {}: lcm({}), gcd({}), mult({})".format(a,b,l,g,m))
            break
    """
