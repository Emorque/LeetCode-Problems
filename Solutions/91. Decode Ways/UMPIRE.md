1. Share questions you would ask to help understand the question:
- By a string a cannot be decoded, could that be when the string only has 0s or a starting zero?
- Will only ints be in the string? No symbols or letters?
- No need to return the decoded messages right? Just the count?
- What is the range of characters in s?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely


3. Write out in plain English what you want to do: 
- I think some backtracking approach can work. 
- Where, starting from some character, we can considered the single character next to be a letter, or the next two chracters a letter
  - If either of these start with 0, then stop as that is not valid 
- This resembles a decision tree, which since there are two decisions made at each character, comes to a complexity of O(2^n)
- A apporoach like fibonacci can be used. There is a base case of 1, but the amount of recursive calls we made is the our n * 1. So that 1 grows depending on n
- In this case, we can have a base case of 1, and add to it everytime, because unless the character is 0, it has a matching letter.
  - And then add again if the character can be between 10-26, when considered the next character
- Then return the current sum, like in fibnonacci

4. Translate each sub-problem into pseudocode:
- Since traversing based on index, have the base case be the len(s) : 1 (len(s)) because the last character needs to be considered, so going + 1 on the last index means we'll land on len(s)
- Can be a list of hashmap

- create traverse helper(index)
  - if s[index] == "0":
    - return 0
  - if index in hashmap:
    - return hashmap[index]

  - decodeNo = travserse(index + 1)
  - if current character can be represented as 10-26
    - decodeNo += travserse(index + 2)
  
  hashmap[index] = decodeNo

  return decodeNo

traverse(0)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def numDecodings(self, s: str) -> int:
        decodings = {} 
        decodings[len(s)] = 1

        def traverse(index):
            if index in decodings:
                return decodings[index]
            if s[index] == "0":
                return 0
            
            decodeNo = traverse(index + 1)
            if index < len(s) - 1 and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
                decodeNo += traverse(index + 2)
            decodings[index] = decodeNo
            return decodeNo
        return traverse(0) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that the usage of decodings, means, that whenever an index is called when it was already called before, then that first if statement returns a value immediately, instead of executing further
- One weak area is that this is not too intuitive, so some more explinations and comments can help explain how I understood this solution built on understanding dp/fibonacci