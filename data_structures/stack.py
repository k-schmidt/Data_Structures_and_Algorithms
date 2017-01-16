"""
Stack
"""


class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == []:
            return True
        return False

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            raise Exception("underflow")
        return self.stack.pop()

if __name__ == '__main__':
    s = Stack()
    s.push(15)
    s.push(6)
    s.push(2)
    s.push(9)
    s.push(17)
    s.push(3)
    print(s.stack)
    s.pop()
    print(s.stack)
