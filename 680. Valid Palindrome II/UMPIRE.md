1. Share 2 questions you would ask to help understand the question:
- Can this be done without creating another data structure?
- Can this be done in O(n) time? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointers (Likely)
- Set (Neutral)
  
3. Write out in plain English what you want to do: 
- What we can use are two pointers, placed at each end that move closer to each other, until they intersect
- However, since there is an additional condition in that: "s can be palindrome after deleting at most one character from it"; we can utilize a boolean variable to remember if we have ignored one character
- If the pointers intersect with this boolean being true or false, return true
- If at any point, the characters the pointers point to are unequal while the variable is true, returned false

- v2:
  - use a helper function with hasIgnored, p1, and p2 as a parameters handle the same logic above. Except, when p1 and p2 don't match, recurively call the helper function twice. Once where p1 moves forward and once where p2 moves forward.
  - make hasIgnored an int, since we still need the function to process if we have ignored one character
  - doing so, we can have two seperate instances. The first version fails cases like:
    - "ebcbbececabbacecbbcbe"

4. Translate each sub-problem into pseudocode:
- Initialize two pointers, p1, p2 at the left and right of s
- Initialize a boolean variable: hasIgnored to false
- Create a while loop that iterates so long as p1 < p2:
  - if p1 == p2:
    - p1++
    - p2--
  - else if p1 != p2 and not hasIgnored:
    - if p1 == p2--:
      - p2--
      - hasIgnored = true
    - else if p1++ == p2:
      - p1++
      - hasIgnored == true
    - else:
      return false
  - else:
    - return false

- v2:
  - isPalindrome(p1, p2, hasIgnored):
    - if hasIgnored > 1:
      - return False
    - while p1 < p2
      - if p1 == p2:
        - p1++
        - p2--
      - else if p1 != p2:
        - return isPalindrome(p1 + 1, p2, hasIgnored+ 1) or isPalindrome(p1, p2 - 1, hasIgnored+ 1)
    - return True

  - return isPalindrome (0, len(s) -1, 0)

5. Translate the pseudocode into Python and share your final answer:
  <!-- 
  class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(p1 : int, p2 : int,  hasIgnored: int) -> bool:
            if hasIgnored > 1:
                return False
            while p1 < p2:
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1 
                else: 
                    return isPalindrome(p1 + 1, p2, hasIgnored + 1) or isPalindrome(p1, p2 - 1, hasIgnored + 1)
            return True
        return isPalindrome(0, len(s) - 1, 0) -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that it utilizes recursion to be able to cover cases like "ebcbbececabbacecbbcbe" that are affected by the ordering of the inner if statements from v1
- One weak area is that it uses a helper function. There are actually some creative solutions that do not do so, and utilize string manipulation to get certain parts of the string.