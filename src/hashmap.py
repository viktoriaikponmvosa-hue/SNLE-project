class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    # -----------------------
    # Hash function
    # -----------------------
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    # -----------------------
    # Load factor
    # -----------------------
    def load_factor(self):
        return self.count / self.size

    # -----------------------
    # Resize when load factor > 0.7
    # -----------------------
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    # -----------------------
    # Insert
    # -----------------------
    def insert(self, key, value):
        idx = self._hash(key)

        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return

        self.table[idx].append((key, value))
        self.count += 1

        if self.load_factor() > 0.7:
            self._resize()

    # -----------------------
    # Search
    # -----------------------
    def search(self, key):
        idx = self._hash(key)

        for k, v in self.table[idx]:
            if k == key:
                return v

        return None

    # -----------------------
    # Delete
    # -----------------------
    def delete(self, key):
        idx = self._hash(key)

        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                self.count -= 1
                return True

        return False