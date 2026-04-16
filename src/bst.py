class Node:
    def __init__(self, cost, path):
        self.cost = cost
        self.path = path
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, cost, path):
        self.root = self._insert(self.root, cost, path)

    def _insert(self, node, cost, path):
        if node is None:
            return Node(cost, path)
        if cost < node.cost:
            node.left = self._insert(node.left, cost, path)
        else:
            node.right = self._insert(node.right, cost, path)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"Cost: {node.cost}, Path: {' -> '.join(node.path)}")
            self.inorder(node.right)