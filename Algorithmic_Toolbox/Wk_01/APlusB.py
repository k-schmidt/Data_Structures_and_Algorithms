# Uses python3
import sys

input = sys.stdin.read(3)
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
