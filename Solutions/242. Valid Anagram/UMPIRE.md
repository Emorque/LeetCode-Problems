1. Share questions you would ask to help understand the question:
- Can another data structure be used?
- Will there be spaces?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash map (Likely)
- Sorting (Likely)

3. Write out in plain English what you want to do:
- For words or phrases to be anagrams, they have to have the same number of character appearances
- So, for rat and car, r appears once for both, a once for both, but only once for t and c. This is not an anagram
- A hash map can be used, where the key is the character and the value is the number of appearances, starting at 0
- The strings will be traversed by the character. For the character in s, the value on the map will be incremented. For the character in t, the value on the map will be decremented
- Then I just have to iterate through the map, and if a value is found not to be 0, then return false
- return True 

4. Translate each sub-problem into pseudocode:
- Itialize a map 
- Iterate through the characters with the length of s
    - If the current char at s is not in the map, initialize it to in the map with a value of 0
    - increment the current char by 1
- Iterate through the characters with the length of t
    - If the current char at t is not in the map, then the False can be returned early
    - decrement the current char by 1
- Iterate through the map
    - If there is a value that is not 0: return False
- Return true once out of the traversal 

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = {}

        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1
        
        for value in hashmap.values():
            if value != 0: return False
        return True -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that there are two places where the algorithm ends early, when the lengths of the string are not equal, and when a character in t is not in s. Once either happens, then False can be returned early
- One weak area is that this could be faster if a counter was imported and used