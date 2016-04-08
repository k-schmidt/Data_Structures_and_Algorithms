# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fib(n):
    list_fibs = [0,1]
    for i in range(2,n+1):
        list_fibs.append(list_fibs[i-1] + list_fibs[i-2])
    return list_fibs[n]

n = int(input())
print(fib(n))
#print(calc_fib(n))
