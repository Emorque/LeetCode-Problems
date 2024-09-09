class TrieNode: 
    def __init__(self):
        self.characters = {}
        self.ends = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.characters:
                temp.characters[c] = TrieNode()
            temp = temp.characters[c]
        temp.ends = True

    def branchOut(self, subWord: str, node: TrieNode):
        temp = node
        for c in range(len(subWord)):
            if subWord[c] in temp.characters:
                temp = temp.characters[subWord[c]]
            elif subWord[c] == '.':
                for key in temp.characters.keys():
                    if self.branchOut(subWord[c + 1:], temp.characters[key]):
                        return True
                return False
            else:
                return False
        return temp.ends

    def search(self, word: str) -> bool:
        return self.branchOut(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)