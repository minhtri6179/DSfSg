##### parent = i // 2
##### left_child = 2 * i
##### right_child = 2 * i + 1
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

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[i] > self.heap[2 * i + 1]
            ):
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    def heapify(self, arr):
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if (
                    2 * i + 1 < len(self.heap)
                    and self.heap[2 * i + 1] < self.heap[2 * i]
                    and self.heap[i] > self.heap[2 * i + 1]
                ):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1


min_heap = MinHeap()
min_heap.push(9)
min_heap.push(2)
min_heap.push(7)
min_heap.push(8)
min_heap.push(4)

while not min_heap.is_empty():
    print(min_heap.pop(), end=" ")


x = [
    1,
    2,
    3,
    4,
    5,
    6,
    100,
    23,
    412,
    123,
    12,
    41,
    23,
    213,
    2154,
    213,
    213,
    123,
    123,
    123,
    123,
    124,
    215,
    436,
    456,
    546,
    45654,
]
min_heap.heapify(x)
print()
while not min_heap.is_empty():
    print(min_heap.pop(), end=" ")
