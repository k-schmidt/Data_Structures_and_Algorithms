# Uses python3
import random

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def max_pairwise_one(list_nums):
    max_num1 = 0
    max_num2 = 0
    for i in list_nums:
        if max_num1 == 0 or i > max_num1:
            max_num1 = i

    if list_nums.count(max_num1) > 1:
        max_num2 = max_num1
    else:
        for j in list_nums:
            if j > max_num2 and j != max_num1:
                max_num2 = j
    return max_num1 * max_num2

def max_pairwise_two(list_nums):
    result = 0
    for i in range(len(list_nums)):
        for j in range(len(list_nums)):
            if a[i] * a[j] > result:
                result = a[i] * a[j]
    return result

"""
while True:
    n = random.randint(1,10)
    print(n)
    a = [random.randint(1, 10) for x in range(n)]
    print(a)
    if max_pairwise_one(a) != max_pairwise_two(a):
        print("Wrong Answer: {0} {1}".format(max_pairwise_one(a),
                                             max_pairwise_two(a)))
        break
    else:
        print("OK")
"""


print(max_pairwise_one(a))
