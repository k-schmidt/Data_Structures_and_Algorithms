# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
n = 10000000
a = [random.randint(1, 1000000000000000000000) for x in xrange

def max_pairwise_one(max=n):
    while i < n:
        a = [random.randint(1,1000000000000) for x in xrange(i)]
        max1 = a.pop(a.index(max(a)))
        max2 = a.pop(a.index(max(a)))

def max_pairwise_two(max=n):
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
                yield result

print(result)
