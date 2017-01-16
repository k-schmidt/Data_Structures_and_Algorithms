"""
Queue
"""


class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        if self.queue == []:
            return True
        return False

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        return self.queue.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(15)
    q.enqueue(6)
    q.enqueue(9)
    q.enqueue(8)
    q.enqueue(4)
    q.enqueue(17)
    q.enqueue(3)
    q.enqueue(5)
    print(q.queue)
    print(q.dequeue())
    print(q.queue)
