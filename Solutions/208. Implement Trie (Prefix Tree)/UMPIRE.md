1. Share questions you would ask to help understand the question:
- Will strings that are extensions or substrings of already entered strings be used?
  - ex: the string is "ending". Is there a chance strings "end" and "endings" are inserted?
- If a string is in the trie, would asking startsWith() with the exact same string return True?
- Can strings like "pppp" be used as inputs?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hashmap (Likely)

3. Write out in plain English what you want to do: 
- Since a trie is a prefix tree, first I thought of a treeNode with its value and left and right child
- With a trie, it seems like one node can have up to 26 nodes as children, one for each character
- I don't think its readable to have 26 seperate values for each node at initialization. 
- Having a hashmap could work as it'll grow when a characters is added to trie when neccessary. 
- And it'll have a quick lookup. 
- And lastly, the search and startsWith means that it'll be important to know when a string ends. 
  - "app" shouldn't return true if "apple" is in the trie
- So our trieNode should have a hashmap with its characters and a boolean "end" to mark that the character is or is not the last character in a string

4. Translate each sub-problem into pseudocode:
- create a trieNode class:
  - init:
    - val = char
    - characters = {}
    - ends = False by default

- init:
  - Intiailize a root trieNode that'll be above all strings
  - self.root = trieNode

- insert:
  - temp = self.root
  - for c in str:
    - if c not in temp.characters:
      - temp.characters[c] = trieNode(c)
    - temp = temp.characters[c]
  - temp.ends = True

  - search:
    - temp = self.root
    - for c in str:
      - if c nor in temp.characters:
        - return False
      - temp = temp.characters[c]
    - return temp.ends
  
  - startsWith:
    - temp = self.root
    - for c in str:
      - if c nor in temp.characters:
        - return False
      - temp = temp.characters[c]
    - return True


5. Translate the pseudocode into Python and share your final answer:
  <!-- class TrieNode:
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
        return True  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a hashmap is used to contain child TrieNodes, allowing to quick lookups with doing search and startsWith
- One weak area is that the TrieNode is not needed. It helps with readability, but the logic can be done within the Trie class itself. 