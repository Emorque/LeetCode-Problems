1. Share questions you would ask to help understand the question:
- What kinds of characters are in s? symbols, letters, numbers?
- What is the range of length for s?
- Can I return a number if I could duplicates? if "aa" exists twice, can I include both in my final count?
- Each character can be considered its own palindrome right?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- 

3. Write out in plain English what you want to do: 
- The brute force way to go about this problem is to get every single possible substring and put it through a ifPalindrome helper function, and everytime True is returned, some final count is incremented
- A less brute force is to treat each character in s as the middle character in a potential palindrome. If the characters to the left and right of the substring are equal, then that is palindrome, and if they aren't, then it is not a palindrome
  - Increment a count each time 
- Do this branching out, for if the current character is in an odd or even length palindrome

4. Translate each sub-problem into pseudocode:
- count = 0
- left, right = 0, 0

- for i in range(len(s)):
  - left, right = i, i

  - while left >= 0 and right < len(s) and s[left] ==s[right]:
    - count += 1
    - left -= 1
    - right += 1

  - left, right = i, i + 1

  - while left >= 0 and right < len(s) and s[left] ==s[right]:
    - count += 1
    - left -= 1
    - right += 1
  
return count

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        left, right = 0, 0

        for i in range(len(s)):
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that, instead of checking each potential substring, this alogirthm only builds ontop of substrings if the current substring is a palindrome
  - If it isn't, then there is no chance adding characters to the left and right turns it into a palindrome
- One weak area is that I do have duplicate code present. I could make a helper function that can then be called twice