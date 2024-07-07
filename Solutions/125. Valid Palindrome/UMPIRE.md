1. Share 2 questions you would ask to help understand the question:
- What should be done if the palindrome is only non-alphanumeric characters?
- Can this be done in O(1) complexity time and space wise?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Pointers (Likely)
- Map(Unlikely)
  
3. Write out in plain English what you want to do:
- We're gonna set two pointers at each end of the string
- We will continually iterate them over the string until they overlap
- Within that loop, check if they have equal characters
  - If they don't, even once, return false
- Once out of the loop, we know its a valid palindrome, so we return true

4. Translate each sub-problem into pseudocode:
- As a base case, if the string is len 0 or 1, just return true 
- What we want to do is set two 'pointers' at each end of the string.
- We then set a while loop that iterates until the two 'pointers' overlap
  - Within the loop, we first check if the 'pointers' are pointing to valid characters
    - if not, then iterate forward (if left pointer) or backward (if right pointer)
  - If they are valid, then compare them as lower-case characters
    - If equal, then iterate forward (if left pointer) or backward (if right pointer)
    - Else, return false
- Once out of the loop, we know its a valid palindrome, so we return true

5. Translate the pseudocode into Python and share your final answer:
  <!-- def isPalindrome(s: str) -> bool:
  if len(s) == 0 or len(s) == 1:
    return True

  p1 = 0
  p2 = len(s) - 1

  while (p1 <= p2):
    while (not (s[p1].isalnum())):
        if (p1 >= p2):
            return True
        p1 += 1
    while (not (s[p2].isalnum())):
        p2 -= 1
    if (s[p1].lower() != s[p2].lower()):
        return False
    p1 += 1
    p2 -= 1
  return True -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it is readable and easy to understand the algorithm
- One weak area is that it could be more optimized with if, elif, else statements