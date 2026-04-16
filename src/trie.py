class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # -----------------------
    # Insert word
    # -----------------------
    def insert(self, word):
        node = self.root

        for ch in word.upper():   # normalize to uppercase
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    # -----------------------
    # Search prefix (autocomplete)
    # -----------------------
    def search_prefix(self, prefix):
        node = self.root

        for ch in prefix.upper():   # normalize input
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []
        self._dfs(node, prefix.upper(), results)
        return results

    # -----------------------
    # DFS to collect words
    # -----------------------
    def _dfs(self, node, prefix, results):
        if node.end:
            results.append(prefix)

        for ch in node.children:
            self._dfs(node.children[ch], prefix + ch, results)