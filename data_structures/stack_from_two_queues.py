"""
Implement a Stack from two queues
"""
from queue import Queue


class Stack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        while len(self.q1.queue) > 1:
            popped = self.q1.dequeue()
            self.q2.enqueue(popped)
        first_out = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return first_out

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(7)
    s.push(8)
    s.push(9)
    print(s.q1.queue)
    print(s.pop())
    print(s.q1.queue, s.q2.queue)
