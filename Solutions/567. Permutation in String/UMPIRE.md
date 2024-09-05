1. Share questions you would ask to help understand the question:
- Are only characters in both strings?
- By permutations, do you mean like an anagram of s1? 

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Sliding Window (Likely)
- Hash map (Likely)

3. Write out in plain English what you want to do: 
- What I want to do is to first traverse through all of s1 so that I can get all of the character frequencies. 
- Why I want this, is because the permutations of s1 mean that the characters in s1 can be in any order, as long as they are consecutive. So, if s1 = "ab", the permuations are "ab" and "ba"
- Then, I want to set up a sliding window technique on s2, where a left pointer starts whenever a character from s1 is found. Then, if the distance between the left and right pointer is equal to the length of s1, then a permutation is found
- However, there will have to be adjustments if the right point either finds a character that occurs more frequently than needed, or a character that is not in the hashmap 

4. Translate each sub-problem into pseudocode:
- Initialize a left pointer that starts at 0, a traversing boolean to false, and a hashmap 
- Iterate through all of s1, putting the character frequencies into the hashmap 
- for i, char in enumerate(s2)
  - if traversing: 
      - if hashmap[char] == 1 and (i - left + 1) == len(s1):
        - return true
      - if char not in hashmap:
        - while left != right 
          - hashmap[s2[left]] += 1
          - left++
      - elif hashmap[char] == 0:
        - while s2[left] != s2[i]:
          - hashmap[s2[left]] += 1
          - left++
        - hashmap[s2[left]] += 1
        - left++
  - if char in hashmap:
    - left = i
    - hashmap[char] -= 1
    - traversing = True
- return False if True was never found

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        traversing = False
        hashmap = {}
        s1Length = len(s1)

        for char in s1:
            hashmap[char] = 1 + hashmap.get(char, 0)
            
        for i, char in enumerate(s2):
            if traversing:
                if char in hashmap and hashmap[char] == 1 and (i - left + 1) == s1Length:
                    return True
                if char not in hashmap:
                    while left != i:
                        hashmap[s2[left]] += 1
                        left += 1
                    traversing = False
                elif hashmap[char] == 0:
                    while s2[left] != char:
                        hashmap[s2[left]] += 1
                        left += 1
                    left += 1
                else:
                    hashmap[char] -= 1
            elif char in hashmap:
                left = i 
                hashmap[char] -= 1
                traversing = True
                if (i - left + 1) == s1Length:
                    return True
        return False  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area about this alogrithm is that it uses a sliding window algorithm to only need to traverse through the s2 once with a loop, with the left pointer catching up depending on character frequency
- One weak area is that this may be difficult to follow, as there is a boolean variable that helps control the left pointer and says that it is currently iterating through a potentially viable substring. 