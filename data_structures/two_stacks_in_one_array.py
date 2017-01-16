"""
Explain how to implement two stacks in one array in such a way that neither stack overflows
unless the total number of elements in both stacks together is n.
"""
from stack import Stack


class Array:

    def __init__(self, max_size=None):
        self.s1 = Stack()
        self.s2 = Stack()
        self.items = [self.s1, self.s2]
        self.max_size = max_size
        self.last_action = None

    def push(self, x):
        if self.max_size is not None and len(self.s1.stack) < (self.max_size / 2):
            self.last_action = self.s1
        else:
            self.last_action = self.s2

        if self.max_size is not None and len(self.s1.stack) + len(self.s2.stack) == self.max_size:
            raise Exception("overflow")
        elif self.max_size is not None and len(self.s1.stack) + len(self.s2.stack) < self.max_size:
            self.last_action.push(x)
        else:
            self.last_action.push(x)

    def pop(self):
        if len(self.s1.stack) == 0:
            raise Exception("underflow")
        elif len(self.s2.stack) == 0:
            self.last_action = self.s1
        popped = self.last_action.pop()
        return popped


if __name__ == '__main__':
    arr = Array(5)
    arr.push(1)
    arr.push(2)
    print(arr.s1.stack, arr.s2.stack)
    print(arr.pop())
    print(arr.s1.stack, arr.s2.stack)
    arr.push(3)
    arr.push(4)
    arr.push(5)
    arr.push(6)
    print(arr.s1.stack, arr.s2.stack)
    print(arr.pop())
    print(arr.pop())
    print(arr.s1.stack, arr.s2.stack)
    print(arr.pop())
    print(arr.s1.stack, arr.s2.stack)
