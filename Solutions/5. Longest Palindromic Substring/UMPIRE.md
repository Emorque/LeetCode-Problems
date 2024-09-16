1. Share questions you would ask to help understand the question:
- Can there be no valid palindromes in s? Would the answer be 1?
- Is s guarenteed to have characters?
- What kind of characters? alpahabetic, numerical, symbols?
- Can there be multiple valid palindromes of the same length?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- DP

3. Write out in plain English what you want to do: 
- Instead of trying a brute-force solution of checking every single possible substring is they palindromes and then returning the max length, 
- I can linearly check each character, and then branch out (going left one and right one), and if the characters here match, the substring is a palindrome, and try to branch out again.
- I can try this by using the starting character (odd length) and starting character + left character (if equal) (even length) as starting substrings 
- At the end, return the substring that has been built with the longest length

4. Translate each sub-problem into pseudocode:
- maxLength = 1
- left, right = 0, 0
- leftI, rightI = 0,0

- for i in range(len(s)):
  - left, right = i, i

  - while left >= 0 and right < len(s) and s[left] == s[right]:
    - left -= 1
    - right += 1
  
  - if (right - left - 1) > maxLength:
    - maxLength = right - left - 1
    - leftI = left + 1
    - rightI = right - 1
  
  - left, right = i, i+1
    - left -= 1
    - right += 1
  
  - while left >= 0 and right < len(s) and s[left] == s[right]:
    - left -= 1
    - right += 1
  
  - if (right - left - 1) > maxLength:
    - maxLength = right - left - 1
    - leftI = left + 1
    - rightI = right - 1

- build the string from leftI, rightI

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        left, right = 0,0
        leftI, rightI = 0, 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if (right - left - 1) > maxLength:
                maxLength = right - left - 1
                leftI = left + 1
                rightI = right - 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if (right - left - 1) > maxLength:
                maxLength = right - left - 1
                leftI = left + 1
                rightI = right - 1
            
        return s[leftI:rightI + 1] -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm builds from the current substring, only if the current substring is a valid palindrome. And it is not longer is, move on to the next character to act as a starting middle character
- One weak area is that there is repeat code, which could be turned into a helper function, since the only differences in the while and if statements, are the starting indexes of left and right