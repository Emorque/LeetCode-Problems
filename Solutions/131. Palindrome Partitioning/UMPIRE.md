1. Share questions you would ask to help understand the question:
- Can a partition be the whole s string?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Backtracking (Likely)
- DFS (Likely)

3. Write out in plain English what you want to do: 
- First, I definetly need a helper function to see if an input string is a palindrome 
- Next, I'll need a dfs helper function that takes in the current subString
- At each step, I need to see all possible palidrome substrings
    - If one is found, I can append it to a list and then call dfs with the rest of the subString
    - after, pop from that list 
    - If just one palindrome is found, then there is at least one possible parition (where you have this one palindrome and then all of the following characters are just a partition of size 1)

4. Translate each sub-problem into pseudocode:
- initialize an output and currList list

- create a palindrome helper function that takes in a string and returns a boolean:
    - p1 = s[0]
    - p2 = len(s) - 1

    - while p1 < p2:
        - if p1 != p2:
            - return False
    - return True

- create a dfs helper function(currIndex, subS)
    - if the current index is equal to the length of s:
        - append a copy of the currList to the output list
    - for i in range(currIndex, len(s)):
        - if isPalindrome(subS[:i + 1]):
            - currList.append(subsS[:i + 1])
            - dfs(currIndex + 1, subS[i + 1:])
            - currList.pop()

- dfs(0, s)
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output, currList = [], []
        sLen = len(s)

        def isPalindrome(subString):
            p1, p2 = 0, len(subString) - 1

            while p1 < p2:
                if subString[p1] != subString[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True

        def dfs(subString):
            if len(subString) == 0: 
                output.append(currList.copy())
                return
            for i in range(len(subString)):
                if isPalindrome(subString[:i + 1]):
                    currList.append(subString[:i + 1])
                    dfs(subString[i + 1:])
                    currList.pop()
        dfs(s)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a backtracking algorithm is used to keep track of previously found palindromes, as they may be present in other partitions
- One weak area is that how I chose to go about this was by passing a part of the string in dfs. If I could improve this, I would try to rework it to work with indexes, saving space and time