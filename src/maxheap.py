class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap)-1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap)-1)
        item = self.heap.pop()
        self._bubble_down(0)
        return item

    def is_empty(self):
        return len(self.heap) == 0

    def _bubble_up(self, i):
        parent = (i-1)//2
        if i > 0 and self.heap[i][0] > self.heap[parent][0]:
            self._swap(i, parent)
            self._bubble_up(parent)

    def _bubble_down(self, i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != i:
            self._swap(i, largest)
            self._bubble_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def enqueue(self, item):
        self.push(item)

    def dequeue(self):
        return self.pop()

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None