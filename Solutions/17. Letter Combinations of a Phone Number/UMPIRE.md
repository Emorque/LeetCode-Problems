1. Share questions you would ask to help understand the question:
- Do the order of digits need to be maintained?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DFS (Likely)

3. Write out in plain English what you want to do: 
- I want to use a dfs funcion that builds a string and passes that current string along to the next digit
- Once the current string is at a length equal to the digits string, I know that the string is completed, and it can be appeneded to an output list 

4. Translate each sub-problem into pseudocode:
- Initialize a hashmap that holds the key: number and a string of its corresponding letters
    - ex: 2: "abc"
- initialize an output list
- create a dfs function(currIndex, currString):
    - if currIndex == len(digits):
        - output.append(currString)
        - return 
    - for c in hashmap[digits[currIndex]]
        - dfs(currIndex + 1, currString + c)
- dfs(0, "")
- return output    

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = []
        digitsLen = len(digits)

        if digitsLen == 0:
            return output

        def dfs(currIndex, currString):
            if currIndex == digitsLen:
                output.append(currString)
                return
            for c in numpad[digits[currIndex]]:
                dfs(currIndex + 1, currString + c)
        dfs(0, "")
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that a dfs solution is used to build a string that ends once the currString's length matches the digits length
- One weak area is that that that a lot of recursive calls get made, one for each letter, so this can get very large space wise compared to something like nested for loops or a queue