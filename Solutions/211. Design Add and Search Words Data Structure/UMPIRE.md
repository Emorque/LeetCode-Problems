1. Share questions you would ask to help understand the question:
- Can there any number of dots within a string?
- When adding a word, will it only contain letters?
- Are the only characters used in the inputs lowercase and '.'?
- What should be returned if when searching, all the characters are found, but there the final character is not the end of a previously entered string?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Trie
- Hashmap 

3. Write out in plain English what you want to do: 
- This looks like a perfect case of using a Trie, since it's usage works great for word storage and lookup
- First, create a TrieNode class
- Then for addWord, append characters into the current node's hashmap and continue iterating 
- For search, follow a similar logic, this time, just checking if characters match 

4. Translate each sub-problem into pseudocode:
- Create a TrieNode class, with the values: 
  - val: char
  - characters: {}

- init:
  - root = empty TrieNode which will hold the start of all strings 

- addWord: 
  - temp = root
  - for c in word:
    - if c not in temp.characters:
      - add c to hashmap
    - temp = temp.characters[c]

- search:
  - temp = root
  - for c in word:
    - if c in temp.characters or c = '.':
      - temp = temp.characters[c]
    - else: 
      - return False
  - return True

  - def branchOut(substring, node): 
    - if substring = ""
      - return True
    - for i in range(substring)
      - if c in temp.characters
        - temp = temp.characters[c]
      - elif c = '.':
        - return branchOut(substring, temp)
      else:
        - return False
    - return True

5. Translate the pseudocode into Python and share your final answer:
  <!-- class TrieNode: 
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
          return self.branchOut(word, self.root) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the logic of Tries and Hashmaps are used an intuitive word search algorithm
- Addiotionally, a recrusive algorithm was made to "branch out" from the current node if a '.' character was found
- One weak area is that if someone is unfamiliar with dfs and tries, this may be hard to follow. Some comments are better variable names could improve readability. 