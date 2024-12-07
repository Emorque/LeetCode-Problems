class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.characters = {}
        self.ends = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.characters:
                temp.characters[c] = TrieNode(c)
            temp = temp.characters[c]
        temp.ends = True

    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.characters:
                return False
            temp = temp.characters[c]
        return temp.ends

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c not in temp.characters:
                return False
            temp = temp.characters[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)