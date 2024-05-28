class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircleQueueLinkedList:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, value):
        tmp = Node(value)
        if self.isEmpty():
            self.rear = tmp
            self.front = tmp
        else:
            if self.rear:
                self.rear.next = tmp
                self.rear = self.rear.next

        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.front:
            tmp = self.front.value
            self.front = self.front.next
        self.size -= 1
        return tmp

    def isEmpty(self):
        return self.size == 0

    def showQueue(self):
        if self.isEmpty():
            return False
        tmp = self.front
        while tmp:
            print(tmp.value, end=" ")
            tmp = tmp.next


q = CircleQueueLinkedList()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.deQueue()
q.deQueue()
q.enQueue(7)
q.enQueue(8)
q.deQueue()
q.deQueue()
q.enQueue(9)
q.enQueue(10)
q.deQueue()
q.deQueue()
q.enQueue(20)
q.enQueue(30)
q.showQueue()
