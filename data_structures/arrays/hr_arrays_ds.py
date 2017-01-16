"""
The first line contains an integer, N (the number of integers in A).
The second line contains N space-separated integers describing A.

Output Format:
Print all N integers A in reverse order as a single line of space-separated integers.

Sample Input:
4
1 4 3 2

Sample Output:
4
2 3 4 1
"""
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(" ")]
index = n-1
while index >= 0:
    print(arr[index], end=" ")
    index -= 1
