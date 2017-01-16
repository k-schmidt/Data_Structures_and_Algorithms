"""
Deque
"""


class Deque:

    def __init__(self):
        self.deque = []

    def is_empty(self):
        if self.deque == []:
            return False
        return True

    def enque_left(self, x):
        self.deque.insert(0, x)

    def enque_right(self, x):
        self.deque.append(x)

    def dequeue_left(self):
        return self.pop(0)

    def dequeue_right(self):
        return self.pop()
