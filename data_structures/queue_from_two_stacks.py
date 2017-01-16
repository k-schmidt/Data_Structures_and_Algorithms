"""
Implementing a queue using two stacks
"""

from stack import Stack


class Queue:

    def __init__(self):
        self.l1 = Stack()
        self.l2 = Stack()

    def enqueue(self, x):
        self.l1.push(x)

    def dequeue(self):
        if self.l2.is_empty():
            while not self.l1.is_empty():
                popped = self.l1.pop()
                self.l2.push(popped)
        return self.l2.pop()

if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(8)
    print(q.l1.stack)
    print(q.dequeue())
    print(q.l1.stack, q.l2.stack)
