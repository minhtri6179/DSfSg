class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircleQueue:
    def __init__(self):
        self.rear = None
        self.front = None
    def en_queue(self, value):
        new_node = Node(value)
        if self.rear == None:
            
