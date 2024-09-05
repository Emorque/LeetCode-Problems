1. Share questions you would ask to help understand the question:
- Can there be more than 2 unique characters in a string?
- Can k be more than the number of characters in a string?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hash map (Likely)
- Sliding Window (Likely)

3. Write out in plain English what you want to do:
- Two pointers can be used to navigate through the string as a sliding window
- As this sliding window grows, how it can be verified as valid, is if the character that appears most has a difference of no more than k than the total number of characters. So if the sliding window has 6 characters and k is 3, and the most frequent character is 3, then the 3 other characters can be adjusted to be viable. If the sliding window has 7 characters, and the most frequent character was still 3, then this window is no longer valid. The left pointer must be adjusted to the left. 
- And every time this window grows, the distance between the two pointers can be used to return the current length of the window. Set this with max() to always keep track of the max possible substring

4. Translate each sub-problem into pseudocode:
- Intialize a hashmap, and left pointer and output variable to 0
- Create a for loop that will iterate through the s string, this will be the right pointer 
  - update the hashmap value for the character key that the right pointer is currently on
  - if the distance between the two pointers - max(hashmap.values()) > k:
    - hashmap[s[left]] -= 1
    - left += 1
  - set output to max(output, i - left + 1) *0 index
- return output

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        output = 0

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
            if (i - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            output = max(output, i - left + 1)
        return output -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area with this algorithm is that since it uses sliding window, there is no need to brute force and check every possible substring in s
- One weak area is that the values in the hashmap has to be checked everytime so as to ensure that the window is viable. While there will be at most 26 keys, it is not the most optimal. 