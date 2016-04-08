# Uses python3
import sys

def get_fibonacci_last_digit(n):
    list_fibs = [0,1]
    for i in range(2, n+1):
        list_fibs.append((list_fibs[i-1] + list_fibs[i-2]) % 10)
    return list_fibs[n]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
