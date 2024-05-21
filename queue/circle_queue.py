class CircleQueue:
    def __init__(self, size):
        self.queue = [-1] * size
        self.size = 0
        self.capacity = size
        self.rear = -1
        self.front = -1

    def en_queue(self, value):
        if self.is_full():
            return False
        elif self.is_empty():
            self.front += 1
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def de_queue(self):
        if self.is_empty():
            return False
        tmp = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return tmp

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_size(self):
        return self.size

    def get_front(self):
        if self.is_empty():
            return False
        return self.queue[self.front]

    def show_queue(self):
        if self.is_empty():
            return False
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            print(self.queue[idx], end=" ")


q = CircleQueue(5)
q.en_queue(1)
q.en_queue(2)
q.en_queue(3)
q.de_queue()
q.en_queue(4)

q.show_queue()
