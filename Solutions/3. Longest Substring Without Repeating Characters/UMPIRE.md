1. Share questions you would ask to help understand the question:
- Can these be a s with have a length of 0?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Two pointer (Likely)
- Hash map (Likely)

3. Write out in plain English what you want to do: 
- What I am thinking, is to use a hash map to store the current characters in the substring
- I will use two pointers, one starting at the left, and one that traverses to the right
- While traversing through the s string, if a character is ecountered that is in the map, the left pointer will go to the right until the repeated characer is found 
- At each step, calculate the distance between the left and right pointers to get the length of the substring 

4. Translate each sub-problem into pseudocode:
- Initialize a hash map, a left pointer, and an output int variable 
- Create a loop to iterate through the s string: 
  - if char is not in the hashmap
    - initialize it to the hashmap with the value: 0
  - if char is in the hashmap:
    - while the left pointer doesn't point to the character the right point is at:
      - delete the key of the character pointed by left from the hashmap
      - left ++ 
    - left++
  - set output to max(output, right - left + 1) (*0 index)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        output = 0
    
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            else:
                while s[left] != s[i]:
                    del hashmap[s[left]]
                    left += 1
                left += 1
            output = max(output, i - left + 1)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that this algorithm uses a two pointer, sliding window solution to have an efficient solution with O(n) space 
- One weak area is that a there could be a better way to rework the del hashmap[s[left]] line. This line bascially ensures that the characters that are skipped for while the left pointer don't get counted in the substring as right progresses