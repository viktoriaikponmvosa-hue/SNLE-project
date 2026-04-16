class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def peek(self):
        return self.data[-1] if self.data else None

    def is_empty(self):
        return len(self.data) == 0