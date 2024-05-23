class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 1

    def push(self, val):
        self.heap.append(val)
        new_idx = len(self.heap) - 1
        while new_idx > 1 and self.heap[new_idx] < self.heap[new_idx // 2]:
            tmp = self.heap[new_idx]
            self.heap[new_idx] = self.heap[new_idx // 2]
            self.heap[new_idx // 2] = tmp
            new_idx = new_idx // 2


min_heap = MinHeap()
min_heap.push(9)
min_heap.push(2)
min_heap.push(7)
min_heap.push(8)
min_heap.push(4)
